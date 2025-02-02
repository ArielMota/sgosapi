from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet, FuncionarioViewSet, OrdemServicoViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet,basename='empresa')
router.register(r'funcionarios', FuncionarioViewSet,basename='funcionario')
router.register(r'ordens-servico', OrdemServicoViewSet,basename='ordem-servico')

urlpatterns = router.urls
