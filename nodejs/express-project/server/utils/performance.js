const { cpuUsage, hrtime } = require('process');

const startingMeasurement = () => {
  const start = hrtime.bigint();
  const getUsage = cpuUsage();

  return {
    time: start,
    usage: getUsage,
  };
};

const endingMeasurement = (start) => {
  const end = hrtime.bigint();
  const time = Number(end - start.time) / 1000000; // Convert nanoseconds to milliseconds

  const elapsedUsage = cpuUsage(start.usage);
  const elapsedUsageMs = elapsedUsage.user / 1000 + elapsedUsage.system / 1000; // Convert microseconds to milliseconds

  let cpuUsagePercent = 0;
  if (time !== 0) {
    cpuUsagePercent = ((elapsedUsageMs / time) * 100).toFixed(2);
  }

  const memUsed = (process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2);

  return {
    time,
    cpuUsagePercent,
    memUsed,
  };
};

module.exports = {
  startingMeasurement,
  endingMeasurement,
};
