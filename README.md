<img width="1854" height="876" alt="image" src="https://github.com/user-attachments/assets/cc6b7a5f-c7c5-4d8a-9436-4834de4df41a" />

# Sysmonitor
Sysmonitor es una aplicación web basada en Django, que permite al usuario ver detalles sobre su equipo, tales como:

## CPU

<img width="1855" height="874" alt="image" src="https://github.com/user-attachments/assets/a94b11bb-e849-480b-a82c-692bb9239454" />

Permite ver el porcentaje de uso del CPU, la cantidad de nucleos (físicos y lógicos), la frecuencia base del procesador, el modelo del procesador y el vendedor del procesador.

## RAM

<img width="1857" height="880" alt="image" src="https://github.com/user-attachments/assets/7117a462-3c06-4bfb-a81d-26982b21f715" />

Permite ver la cantidad total de RAM, la cantidad usada, la cantidad disponible y el porcentaje de uso.

## Disco

<img width="1857" height="864" alt="image" src="https://github.com/user-attachments/assets/870f19f6-9cca-4855-bfab-259f929ee058" />

Muestra al usuario el nombre de la unidad principal, su punto de montaje, la cantidad total de almacenamiento, el espacio libre y usado, el sistema de archivos y el porcentaje de uso de la unidad.

## Información del Sistema

<img width="1855" height="869" alt="image" src="https://github.com/user-attachments/assets/53c60817-4548-4376-95e2-eacf4b12a6ae" />

Muestra el nombre del sistema operativo junto a su version, versión de lanzamiento (e.g: "Windows 10", "Windows 11", "Linux 7.0-rc1"), arquitectura y el tiempo transcurrido desde el arranque del sistema.

## Instalación

Hay dos formas de ejecutar la aplicación:

### Clonar repositorio y crear imagen con Docker

```
git clone https://github.com/anpert70y/resource-manager.git
cd resource-manager
docker build -t sysmonitor
docker run -d sysmonitor -p 8000:8000
```

### Pull del paquete con Docker

```
docker pull ghcr.io/anpert70y/resource-manager:latest
docker tag ghcr.io/anpert70y/resource-manager:latest sysmonitor:latest
docker run -d sysmonitor:latest -p 8000:8000
```

Luego de esto, la aplicación estara disponible en localhost:8000.


