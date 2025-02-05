
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasALuno, ListaAlunosMatriculados
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router= routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursoViewSet, basename='Cursos' )
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

                
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas', ListaMatriculasALuno.as_view()), 
    path('curso/<int:pk>/matriculas', ListaAlunosMatriculados.as_view()),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

