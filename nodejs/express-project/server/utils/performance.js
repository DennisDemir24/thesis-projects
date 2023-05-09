import {cpuUsage, memoryUsage} from 'process'

export const startingMeasurment = () => {
    const start = new Date()

    const getUsage = cpuUsage()

    return {
        time: start,
        usage: getUsage
    }
}

export const endingMeasurment = (start) => {
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