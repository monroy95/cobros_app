# App cobros automaticos
Aplicacion para generar cobros diariamente

> La Funcion de tareas programadas solo funciona en sistemas basados en linux

## Instalar
### Crear y activar entorno virtual

**Crear**
```bash
virtualenv [virtual-env-name] -p python3
```
**activar**

```bash
source virtual_env_name/bin/activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

## Configure el correo electronico
Esto para el envio automatico de correos. Se puede realizar en el archivo `settings.py` en las variables

```python
EMAIL_HOST_USER = 'ingrese el correo electronico'
EMAIL_HOST_PASSWORD = 'ingrese su contrasenia'
```

## Validar que cron este activo
**Ver status del servicio cron**
```bash
sudo service cron status
```

**Arrancar servicio**
```bash
sudo service cron start
```

**Detener servicio**
```bash
sudo service cron stop
```

## Programe las tareas
**Programar tareas**
```bash
python manage.py crontab add
```

**Mostrar que tareas se encuentran programadas**
```bash
python manage.py crontab show
```

**Remover tareas programadas**
```bash
python manage.py crontab remove
```

**Ingresar al admin**
**Ejecute la Aplicacion con**
```bash
python manage.py runserver
```

**Desde el navegador ingrese con**
user: mario
password: armada.dev


## Funcionamiento
Una vez este dentro del administrator, cree usuarios con datos en todos los campos y correos electronicos validos.

Segun la frecuencia de la tarea programadas, se verifica que usuario aun aplican para realizarles un cobro automatico,
si el usuario aplica y tiene un metodo de pago valido se crear un registro en `Charges` y se envia un correo electronico
con el status del proceso
