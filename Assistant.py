from ITassistant.models import Equipos
import psutil

class Datos_Equipos():
    def __init__(self):
        self.cpu_equipo={
    'uso_CPU':psutil.cpu_percent(interval=0.1, percpu=True),
    'nucleos_logicos':psutil.cpu_count(logical=False),
    'nucleos_fisicos':psutil.cpu_count(logical=True),
    'frecuencia_actual':psutil.cpu_freq(percpu=False)[0],
    'frecuencia_minima':psutil.cpu_freq(percpu=False)[1],
    'frecuencia_maxima': psutil.cpu_freq(percpu=False)[2],
    'temperatura_actual':psutil.sensors_temperatures(fahrenheit=False)['coretemp'][0][1],
    'temperatura_alta':psutil.sensors_temperatures(fahrenheit=False)['coretemp'][0][2],
    'temperatura_critica':psutil.sensors_temperatures(fahrenheit=False)['coretemp'][0][3]
    }
        self.ram_equipo={
        'capacidad_ram':psutil.virtual_memory()[0],
        'porcentaje_ram':psutil.virtual_memory().percent,
        'uso_ram':psutil.virtual_memory()[3],
        'disponibilidad_ram':psutil.virtual_memory()[1]
    }
        self.almacenamiento_equipo={
        'capacidad_disco':psutil.disk_usage('/')[0],
        'porcentaje_disco': psutil.disk_usage('/').percent,
        'uso_disco':psutil.disk_usage('/')[1],
        'disponibilidad_disco': psutil.disk_usage('/')[2]
    }
        self.info_equipo={
    'nombre_equipo':psutil.users()[0][0],
    'nombre_usuario':psutil.users()[1][0],
    'estado_usuario':psutil.users()[0][2],
    'pid':psutil.users()[0][4],
    'ip':psutil.net_if_addrs()['wlo1'][0][1],
    'mascara_red': psutil.net_if_addrs()['wlo1'][0][2]
    }
    
    def recoleccion_datos(self):
        self.cpu_equipo
        self.ram_equipo
        self.almacenamiento_equipo
        self.info_equipo
    
    def revision_datos(self):

        print('')
        print('Datos del CPU'.center(24,'*'))
        print('')

        for clave, valor in self.cpu_equipo.items():
            if clave=='frecuencia_actual'or clave=='frecuencia_minima'or clave=='frecuencia_maxima':
                print(f'> {clave} = {valor:.2f} Hz')
            elif clave=='temperatura_actual' or clave=='temperatura_alta' or clave=='temperatura_critica':
                print(f'> {clave} = {valor:.2f}°C ')
            else:
                print(f'> {clave} = {valor}')
        
        def gigabytes(unidad):
            return unidad / 1024**3
        
        print('')
        print('Datos de la memoria ram'.center(45, '*'))
        print('')

        for clave, valor in self.ram_equipo.items():
            if clave == 'porcentaje_ram':
                print('> {} = {:.2f}%'.format(clave,valor))
            print('> {} = {:.2f}GB'.format(clave,gigabytes(valor)))

        print('')
        print('Datos del almacenamiento'.center(47, '*'))
        print('')

        for clave, valor in self.almacenamiento_equipo.items():
            if clave == 'porcentaje_disco':
                print('> {} = {:.2f} %'.format(clave,valor))    
            print('> {} = {:.2f} GB'.format(clave,gigabytes(valor)))

        print('')
        print('Información del equipo'.center(43,'*'))
        print('')

        for clave, valor in self.info_equipo.items(): 
            print('> {} = {}'.format(clave,valor))

    def envio_datos(self):
        
        def gigabytes(unidad):
            return unidad / 1024**3
        
        equipo= Equipos(
        Uso_CPU='{}'.format(self.cpu_equipo['uso_CPU']),
        Nucleos_logicos='{}'.format(self.cpu_equipo['nucleos_logicos']),
        Nucleos_fisicos='{}'.format(self.cpu_equipo['nucleos_fisicos']),
        Frecuencia_actual='{:.2f} Hz'.format(self.cpu_equipo['frecuencia_actual']),
        Frecuencia_minima='{:.2f} Hz'.format(self.cpu_equipo['frecuencia_minima']),
        Frecuencia_maxima='{:.2f} Hz'.format(self.cpu_equipo['frecuencia_maxima']),
        Temperatura_actual='{} °C'.format(self.cpu_equipo['temperatura_actual']),
        Temperatura_alta='{} °C'.format(self.cpu_equipo['temperatura_alta']),
        Temperatura_critica='{} °C'.format(self.cpu_equipo['temperatura_critica']),
        Capacidad_RAM ='{:.2f} GB'.format(gigabytes(self.ram_equipo['capacidad_ram'])),
        Porcentaje_RAM ='{:.2f} %'.format(self.ram_equipo['porcentaje_ram']),
        Uso_RAM ='{:.2f} GB'.format(gigabytes(self.ram_equipo['uso_ram'])),
        Disponibilidad_RAM ='{:.2f} GB'.format(gigabytes(self.ram_equipo['disponibilidad_ram'])),
        Capacidad_disco='{:.2f} GB'.format(gigabytes(self.almacenamiento_equipo['capacidad_disco'])),
        Porcentaje_disco='{:.2f} %'.format(self.almacenamiento_equipo['porcentaje_disco']),
        Uso_disco='{:.2f} GB'.format(gigabytes(self.almacenamiento_equipo['uso_disco'])),
        Disponibilidad_disco='{:.2f} GB'.format(gigabytes(self.almacenamiento_equipo['disponibilidad_disco'])),
        Equipo=self.info_equipo['nombre_equipo'],
        Usuario=self.info_equipo['nombre_usuario'],
        Estado_usuario=self.info_equipo['estado_usuario'],
        PID=self.info_equipo['pid'],
        IP=self.info_equipo['ip'],
        Mascara_red=self.info_equipo['mascara_red']
    )
        equipo.save()

equipo = Datos_Equipos()
equipo.recoleccion_datos()
equipo.revision_datos()
equipo.envio_datos()