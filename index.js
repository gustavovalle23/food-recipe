const express = require('express')
const app = express()
const port = 3000

app.get('/users/:id', async (req, res) => {
	const { id } = req.params
})

app.listen(port, () => {
	console.log(`Example app listening on port ${port}`)
})
