const express = require('express')
const serveStatic = require('serve-static')
const path = require('path')

const app = express()

app.use('/', serveStatic(path.join(__dirname, '/dist')))

const port = process.env.PORT || 8080
app.listen(port)

console.log('Listening on port ' + port)
//npm run build
//npm install express serve-static --save
//poner el server.js y crear el comandos en el package.json
//quitar el /dist del gitignore
//heroku login
//heroku git:remote -a buscador-alumnos-uni
//o sino git remote remove origin y git remote add origin git@github.com:TheBestShooter/buscador-alumnos-uni.git
//git add .
//git commit -m ""
//git push heroku master -f