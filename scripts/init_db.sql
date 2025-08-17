create table if not exists users (
  id bigint primary key,                 -- tg_user_id
  username text,
  first_name text,
  tz text not null default 'Europe/Kyiv',
  notify_time time not null default '09:00',
  days_selected smallint[] not null default '{2,5}', -- вт=2, пт=5 (ISO, пн=1)
  pre_reminder boolean not null default false,
  created_at timestamptz not null default now()
);

create table if not exists plants (
  id bigserial primary key,
  user_id bigint not null references users(id) on delete cascade,
  display_name text not null,
  species_key text,
  location_note text,
  active boolean not null default true,
  created_at timestamptz not null default now()
);

create table if not exists care_profiles (
  species_key text primary key,
  water_every_days int,
  fertilize_every_days int,
  wipe_every_days int,
  repot_months int,
  notes text
);

create table if not exists user_care_overrides (
  plant_id bigint references plants(id) on delete cascade,
  key text not null,
  value text not null,
  primary key (plant_id, key)
);

create table if not exists user_settings (
  user_id bigint primary key references users(id) on delete cascade,
  mode text not null default 'standard'  -- standard | strict_group | mixed
);

create table if not exists tasks (
  id bigserial primary key,
  user_id bigint not null references users(id) on delete cascade,
  plant_id bigint not null references plants(id) on delete cascade,
  task_type text not null,               -- water | fertilize | wipe | repot
  due_date date not null,
  status text not null default 'planned',-- planned | done | postponed
  origin text not null default 'profile',-- profile | grouped
  last_reminded_at timestamptz
);
