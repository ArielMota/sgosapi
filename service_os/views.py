from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import Empresa, Funcionario, OrdemServico
from .permissions import IsEmpresaOrReadOnly, IsFuncionarioAssignedOrReadOnly, EmpresaCustomPermission
from .serializers import EmpresaSerializer, FuncionarioSerializer, OrdemServicoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    """
        Permite criar uma empresa sem autenticação.
        Apenas usuários administradores poderão realizar a ação de deletar uma empresa
        """
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [EmpresaCustomPermission]




class FuncionarioViewSet(viewsets.ModelViewSet):
    """
        Apenas empresas podem criar funcionários, mas os próprios funcionários podem visualizar seus dados.
        """

    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAuthenticated,IsEmpresaOrReadOnly]  # Exige que o usuário esteja autenticado

class OrdemServicoViewSet(viewsets.ModelViewSet):
    """
    Empresas podem criar e editar ordens de serviço.
    Funcionários só podem visualizar ou modificar as OS atribuídas a eles.
    """

    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    permission_classes = [IsAuthenticated,IsEmpresaOrReadOnly | IsFuncionarioAssignedOrReadOnly]  # Exige que o usuário esteja autenticado
