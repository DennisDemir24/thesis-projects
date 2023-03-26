const {cpuUsage, memoryUsage} = require('process')

const startingMeasurment = () => {
    const start = new Date()

    const getUsage = cpuUsage()

    return {
        time: start,
        usage: getUsage
    }
}

const endingMeasurment = (start) => {
    const end = new Date()
    const time = end.getTime() - start.time.getTime()
    const cpuUsed = cpuUsage(start.usage).user / 1000
    const memUsed = (memoryUsage().heapUsed / 1024 / 1024).toFixed(2)

    return {
        time,
        cpuUsed,
        memUsed
    }


}

module.exports = {
    startingMeasurment,
    endingMeasurment
}