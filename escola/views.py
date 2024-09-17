from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated 
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import cache_page 


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    

class CursoViewSet(viewsets.ModelViewSet):
    """Exbindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer 
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculaViewSet(viewsets.ModelViewSet):
     """Listando todas as matriculas"""
     queryset =Matricula.objects.all()
     serializer_class=MatriculaSerializer
     http_method_names = ['get', 'post', 'put', 'path']
     authentication_classes = [BasicAuthentication]
     permission_classes = [IsAuthenticated]
     
     @method_decorator(cache_page(20))
     def dispatch(self, *args, **kwargs):
         return super(MatriculaViewSet, self).dispatch(*args, **kwargs)
    
    
class ListaMatriculasALuno(generics.ListAPIView):
   """Listando as matriculas de um aluno ou aluna"""
   def get_queryset(self):
       queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
       return queryset
   serializer_class = ListaMatriculasAlunoSerializer
   authentication_classes = [BasicAuthentication]
   permission_classes = [IsAuthenticated]
   
   
class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
        
        