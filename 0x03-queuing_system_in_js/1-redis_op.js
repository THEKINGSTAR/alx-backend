import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  return(`Redis client not connected to the server: ${err.message}`);
});


client.on('connect', () => {
  return('Redis client connected to the server');
});

