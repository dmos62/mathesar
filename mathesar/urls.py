from django.urls import include, path
from rest_framework_nested import routers

from mathesar import views
from mathesar.api.viewsets.columns import ColumnViewSet
from mathesar.api.viewsets.constraints import ConstraintViewSet
from mathesar.api.viewsets.data_files import DataFileViewSet
from mathesar.api.viewsets.databases import DatabaseViewSet
from mathesar.api.viewsets.records import RecordViewSet
from mathesar.api.viewsets.schemas import SchemaViewSet
from mathesar.api.viewsets.tables import TableViewSet


router = routers.DefaultRouter()
router.register(r'tables', TableViewSet, basename='table')
router.register(r'schemas', SchemaViewSet, basename='schema')
router.register(r'databases', DatabaseViewSet, basename='database')
router.register(r'data_files', DataFileViewSet, basename='data-file')

table_router = routers.NestedSimpleRouter(router, r'tables', lookup='table')
table_router.register(r'records', RecordViewSet, basename='table-record')
table_router.register(r'columns', ColumnViewSet, basename='table-column')
table_router.register(r'constraints', ConstraintViewSet, basename='table-constraint')

urlpatterns = [
    path('api/v0/', include(router.urls)),
    path('api/v0/', include(table_router.urls)),

    # Specifying each route individually to facilitate redirection and data pre-rendering based on route
    path('', views.home, name="home"),
    path('<db_name>/', views.db_home, name="db_home"),
    path('<db_name>/schemas/', views.schemas, name="schemas"),
    path('<db_name>/<int:schema_id>/', views.schema_home, name="schema_home"),
]
