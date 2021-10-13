const express = require('express')
const app = express()
const port = 3000
const ejs = require('ejs')

app.set('view engine', 'ejs')

app.get('/', (req, res) => {
    res.render('index.ejs')
})

app.get('/form', (req, res) => {
    res.render('form.ejs')
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})