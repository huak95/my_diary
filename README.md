# my_diary

```bash
conda activate mydiary
python manage.py runserver
```

http://127.0.0.1:8000/

## DOCKER
```bash
docker build . -t "saksorn_notes"
docker run -it -p 9595:9595 --rm saksorn_notes /bin/bash

# push and tag
docker tag saksorn_notes saksornr/saksorn_notes
docker push saksornr/saksorn_notes
```