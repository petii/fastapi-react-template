# Quick project with Python-FastAPI backend and Parcel-React frontend

## Backend

(set up a virtual enviroment)
```bash
 > pip install -r requirements.txt
    ...
 > uvicorn server:app [--reload]
```

To start the backend server. (add --reload if do not want to restart it after )

## Frontend

```bash
 > cd app
 > yarn install
    ... 
 > yarn parcel src/index.html
```

To start serving the React application.

Building with `yarn parcel build --public-url ./ src/index.html` puts the site in `app/dist` and you can then reach it on `<backend>/app`/