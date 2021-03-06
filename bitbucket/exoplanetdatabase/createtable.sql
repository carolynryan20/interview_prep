DROP TABLE IF EXISTS exoplanets;
CREATE TABLE exoplanets (
  planet_name varchar(50),
  mass real,
  radius real,
  orbital_period real,
  semi_major_axis real,
  eccentricity real,
  inclination real,
  angular_distance real,
  discovered smallint,
  updated date,
  omega real,
  tperi float,
  temp_calculated real,
  temp_measured real,
  publication_status varchar(50),
  detection_type varchar(50),
  mass_detection_type varchar(50),
  radius_detection_type varchar(50),
  molecules varchar(200),
  star_name varchar(50),
  ra float,
  declination float,
  mag_v real,
  star_distance real,
  star_metallicity real,
  star_mass real,
  star_radius real,
  star_sp_type varchar(25),
  star_age real,
  star_temp real

);