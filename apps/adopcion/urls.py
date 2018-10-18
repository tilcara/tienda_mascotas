
from django.conf.urls import url
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
	
	url(r'^index$', index_adopcion),
	url(r'^solicitud/listar$', login_required(SolicitudList.as_view()),name='solicitud_listar'),
	url(r'^solicitud/nueva$', login_required(SolicitudCreate.as_view()),name='solicitud_crear'),
	url(r'^solicitud/editar/(?P<pk>\d+)$', login_required(SolicitudUpdate.as_view()),name='solicitud_editar'),
	url(r'^solicitud/eliminar/(?P<pk>\d+)$', login_required(SolicitudDelete.as_view()),name='solicitud_eliminar'),

]
