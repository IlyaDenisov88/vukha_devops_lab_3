# Лабораторная 3

## Задание:
Реализовать автоматическую сборку докер образа в репризиторий после пуша, а также сохранение результата его сборки.

## Выполнение работы:
Автоматическую сборку будем реализовывать при помощи Github Actions.

### 1. Создание репозитория
Для начала, создадим Dockerfile и простой файл Python, который записывает числа в текстовый файл numbers.txt

- **Dockerfile**
  
![repository](https://github.com/IlyaDenisov88/vukha_devops_lab_3/assets/113051806/329e403d-b4a0-45d7-b832-f81c69fceb23)
- **printer.py**
  
![printer](https://github.com/IlyaDenisov88/vukha_devops_lab_3/assets/113051806/118f54e9-9c25-48d8-a35a-d49395cdd4d5)
- **numbers.txt**
  
![numbers](https://github.com/IlyaDenisov88/vukha_devops_lab_3/assets/113051806/6e98045e-0ed0-4754-b06a-5200b77b3f78)

### 2. Создание Docker image с помощью yml файла
Создадим новый Docker image workflow по шаблону из Github Actions и отредактируем его для корректной автосборки.

- **yml file**

![изображение_2023-11-13_205251707](https://github.com/IlyaDenisov88/vukha_devops_lab_3/assets/113051806/28bdd9a2-47a8-4037-b9be-e5c37081f009)

Изменим имя Docker image:
```
- run: docker build . --file Dockerfile --tag krokodile888/dogcat:latest
```
Создадим скрипт для пуша, в котором будем подсоединяться к DockerHub:
```
- name: Push the Docker image
      run: docker login -u krokodile888 -p ${{ secrets.DOCKER_TOKEN }} && docker push krokodile888/dogcat:latest
```

### 3. Создание токена
В ранее созданном скрипте в качестве пароля используется Github Secret, который необходимо создать в настройках Actions Secrets. В поле value нужно указать токен, сгенерированный на DockerHub.
- **DOCKER_TOKEN**

![image](https://github.com/IlyaDenisov88/vukha_devops_lab_3/assets/113051806/7bc3a2eb-602b-45db-930e-2c9e8b11822e)

После этого докер образ будет автоматически собран и сохранен на DockerHub при пуше в репризиторий.

- **DockerHub page**

![изображение_2023-11-13_210432471](https://github.com/IlyaDenisov88/vukha_devops_lab_3/assets/113051806/125e8b6c-5369-4089-8253-0ddbe770ca1f)
