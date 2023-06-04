import { cpuUsage } from 'process';

export const startingMeasurement = () => {
  const start = new Date();
  const getUsage = process.cpuUsage();

  return {
    time: start,
    usage: getUsage,
  };
};

export const endingMeasurement = (start) => {
  const end = new Date();
  const time = end.getTime() - start.time.getTime();

  const elapsedUsage = process.cpuUsage(start.usage);
  const elapsedUsageMs = elapsedUsage.user + elapsedUsage.system;
  const totalUsageMs = time * 1000;
  const cpuUsagePercent = ((elapsedUsageMs / totalUsageMs) * 100).toFixed(2);

  const memUsed = (process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2);

  return {
    time,
    cpuUsagePercent,
    memUsed,
  };
};
