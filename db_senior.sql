PGDMP             
             {         	   db-senior    14.2    14.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    24576 	   db-senior    DATABASE     j   CREATE DATABASE "db-senior" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE "db-senior";
                postgres    false            �            1255    24677    update_utc()    FUNCTION       CREATE FUNCTION public.update_utc() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
UPDATE public."alarm"
set start_date_utc = NEW.start_date_utc at time zone 'utc',
end_date_utc = NEW.end_date_utc at time zone 'utc'
where id = NEW.id;
RETURN NULL;
END;
$$;
 #   DROP FUNCTION public.update_utc();
       public          postgres    false            �            1259    24699    alarm    TABLE     7  CREATE TABLE public.alarm (
    id integer NOT NULL,
    alarm_name character varying(30) NOT NULL,
    comment character varying(40),
    start_date date NOT NULL,
    end_date date,
    start_date_utc timestamp with time zone,
    end_date_utc timestamp with time zone,
    is_delete boolean DEFAULT false
);
    DROP TABLE public.alarm;
       public         heap    postgres    false            �            1259    24698    alarm_id_seq    SEQUENCE     �   CREATE SEQUENCE public.alarm_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.alarm_id_seq;
       public          postgres    false    210            �           0    0    alarm_id_seq    SEQUENCE OWNED BY     =   ALTER SEQUENCE public.alarm_id_seq OWNED BY public.alarm.id;
          public          postgres    false    209            ]           2604    24702    alarm id    DEFAULT     d   ALTER TABLE ONLY public.alarm ALTER COLUMN id SET DEFAULT nextval('public.alarm_id_seq'::regclass);
 7   ALTER TABLE public.alarm ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    209    210            �          0    24699    alarm 
   TABLE DATA           w   COPY public.alarm (id, alarm_name, comment, start_date, end_date, start_date_utc, end_date_utc, is_delete) FROM stdin;
    public          postgres    false    210   W       �           0    0    alarm_id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.alarm_id_seq', 5, true);
          public          postgres    false    209            `           2606    24707    alarm alarm_alarm_name_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.alarm
    ADD CONSTRAINT alarm_alarm_name_key UNIQUE (alarm_name);
 D   ALTER TABLE ONLY public.alarm DROP CONSTRAINT alarm_alarm_name_key;
       public            postgres    false    210            b           2606    24705    alarm pk_id 
   CONSTRAINT     I   ALTER TABLE ONLY public.alarm
    ADD CONSTRAINT pk_id PRIMARY KEY (id);
 5   ALTER TABLE ONLY public.alarm DROP CONSTRAINT pk_id;
       public            postgres    false    210            c           2620    24708    alarm trigger_update_utc    TRIGGER     r   CREATE TRIGGER trigger_update_utc AFTER INSERT ON public.alarm FOR EACH ROW EXECUTE FUNCTION public.update_utc();
 1   DROP TRIGGER trigger_update_utc ON public.alarm;
       public          postgres    false    211    210            �   g   x�M�1� �ṽ����.&0���h��!uh��o�G���:֖�=���H��[w#+��Y3XT�g��X����#<�d4�ZQ+��kw���mB���0�     