### Local MySQL environment

This is just a MySQL container with some extra tooling for running migrations and backing up data:

- `./scripts`: Scripts for running migrations and backing up data.
- `./schema/init`: SQL scripts for creating databases in the container.
- `./docker`: Docker files
- `./data`: git-ignored backup data for loading into the container schema

---

### Setup

This assumes that you already have docker & docker-compose installed: https://docs.docker.com/v17.12/install/

1. Create a network: `docker network create default_network`
1. From `./docker`: `docker-compose up --build`

The container should now be running on localhost:3306 with user/pass == root/password.

---

### Using the helper scripts

Run all of the following from `./scripts`

- To create a new schema: `./create_schema schema_name`
- To run migrations : `./run_migrations`

---