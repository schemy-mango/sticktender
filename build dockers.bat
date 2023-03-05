cd backend
docker build -t mybackend .
docker run -p 8000:8000 mybackend

cd ../frontend
docker build -t myfrontend .
docker run -p 3000:3000 myfrontend
