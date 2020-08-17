PGDMP     %                    x            siam    11.7    11.7 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                        1262    41591    siam    DATABASE     �   CREATE DATABASE siam WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Spain.1252' LC_CTYPE = 'Spanish_Spain.1252';
    DROP DATABASE siam;
             postgres    false                       0    0    DATABASE siam    COMMENT     <   COMMENT ON DATABASE siam IS 'última base de datos creada';
                  postgres    false    3072            �            1259    49788    Beneficiarios    TABLE     2  CREATE TABLE public."Beneficiarios" (
    "tipoDNI" character varying(1) NOT NULL,
    dni integer NOT NULL,
    nombre character varying(20) NOT NULL,
    apellidos character varying(30) NOT NULL,
    afiliado character varying(1) NOT NULL,
    "nroAfiliado" integer,
    localidad_id integer NOT NULL
);
 #   DROP TABLE public."Beneficiarios";
       public         postgres    false            �            1259    57990    CM_brinda_Especialidades    TABLE     �   CREATE TABLE public."CM_brinda_Especialidades" (
    id integer NOT NULL,
    "centroMedico_id" character varying(13) NOT NULL,
    especialidades_id integer NOT NULL
);
 .   DROP TABLE public."CM_brinda_Especialidades";
       public         postgres    false            �            1259    57988    CM_brinda_Especialidades_id_seq    SEQUENCE     �   CREATE SEQUENCE public."CM_brinda_Especialidades_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public."CM_brinda_Especialidades_id_seq";
       public       postgres    false    227                       0    0    CM_brinda_Especialidades_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public."CM_brinda_Especialidades_id_seq" OWNED BY public."CM_brinda_Especialidades".id;
            public       postgres    false    226            �            1259    49801    Centros médicos    TABLE     O  CREATE TABLE public."Centros médicos" (
    "cuitCM" character varying(13) NOT NULL,
    "razonSocial" character varying(50) NOT NULL,
    domicilio character varying(100) NOT NULL,
    telefono character varying(50) NOT NULL,
    horario text NOT NULL,
    e_mail character varying(50) NOT NULL,
    localidad_id integer NOT NULL
);
 &   DROP TABLE public."Centros médicos";
       public         postgres    false            �            1259    49853    Diagnostico    TABLE     j   CREATE TABLE public."Diagnostico" (
    codigo character varying(4) NOT NULL,
    nombre text NOT NULL
);
 !   DROP TABLE public."Diagnostico";
       public         postgres    false            �            1259    49831    DoctorTieneEspecialidades    TABLE     �   CREATE TABLE public."DoctorTieneEspecialidades" (
    id integer NOT NULL,
    horario character varying(250) NOT NULL,
    doctor_id character varying(13) NOT NULL,
    especialidad_id integer NOT NULL
);
 /   DROP TABLE public."DoctorTieneEspecialidades";
       public         postgres    false            �            1259    49816    Doctores    TABLE     �  CREATE TABLE public."Doctores" (
    "matriculaDoc" integer NOT NULL,
    cuit character varying(13) NOT NULL,
    nombre character varying(30) NOT NULL,
    apellidos character varying(30) NOT NULL,
    telefono character varying(30) NOT NULL,
    domicilio character varying(30) NOT NULL,
    email character varying(30) NOT NULL,
    "convenioOSECAC" character varying(1) NOT NULL
);
    DROP TABLE public."Doctores";
       public         postgres    false            �            1259    49821    Especialidades    TABLE     �   CREATE TABLE public."Especialidades" (
    "idEspecialidad" integer NOT NULL,
    nombre character varying(30) NOT NULL,
    descripcion text NOT NULL
);
 $   DROP TABLE public."Especialidades";
       public         postgres    false            �            1259    49783    Localidades    TABLE     t   CREATE TABLE public."Localidades" (
    codigopostal integer NOT NULL,
    nombre character varying(30) NOT NULL
);
 !   DROP TABLE public."Localidades";
       public         postgres    false            �            1259    49870    PedidosAmbulatorios    TABLE     �   CREATE TABLE public."PedidosAmbulatorios" (
    "idPedido" integer NOT NULL,
    fecha_ingreso date NOT NULL,
    beneficiario_id integer NOT NULL
);
 )   DROP TABLE public."PedidosAmbulatorios";
       public         postgres    false            �            1259    49877    PracticasDelPedido    TABLE     j  CREATE TABLE public."PracticasDelPedido" (
    fecha_prescripcion date NOT NULL,
    autorizado character varying(1) NOT NULL,
    "importeCoseguro" double precision,
    observaciones text,
    diagnosticos_id integer NOT NULL,
    doctores_id character varying(13) NOT NULL,
    practicas_id integer NOT NULL,
    pedido_ambulatorio_ptr_id integer NOT NULL
);
 (   DROP TABLE public."PracticasDelPedido";
       public         postgres    false            �            1259    41623 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         postgres    false            �            1259    41621    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public       postgres    false    203                       0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
            public       postgres    false    202            �            1259    41633    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         postgres    false            �            1259    41631    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public       postgres    false    205                       0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
            public       postgres    false    204            �            1259    41615    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         postgres    false            �            1259    41613    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public       postgres    false    201                       0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
            public       postgres    false    200            �            1259    41641 	   auth_user    TABLE     �  CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
    DROP TABLE public.auth_user;
       public         postgres    false            �            1259    41651    auth_user_groups    TABLE        CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         postgres    false            �            1259    41649    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public       postgres    false    209                       0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
            public       postgres    false    208            �            1259    41639    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public       postgres    false    207                       0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
            public       postgres    false    206            �            1259    41659    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         postgres    false            �            1259    41657 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public       postgres    false    211                       0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
            public       postgres    false    210            �            1259    41719    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         postgres    false            �            1259    41717    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public       postgres    false    213            	           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
            public       postgres    false    212            �            1259    41605    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         postgres    false            �            1259    41603    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public       postgres    false    199            
           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
            public       postgres    false    198            �            1259    41594    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         postgres    false            �            1259    41592    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public       postgres    false    197                       0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
            public       postgres    false    196            �            1259    41750    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         postgres    false            �            1259    49829 '   doctores_doctortieneespecialidad_id_seq    SEQUENCE     �   CREATE SEQUENCE public.doctores_doctortieneespecialidad_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE public.doctores_doctortieneespecialidad_id_seq;
       public       postgres    false    221                       0    0 '   doctores_doctortieneespecialidad_id_seq    SEQUENCE OWNED BY     n   ALTER SEQUENCE public.doctores_doctortieneespecialidad_id_seq OWNED BY public."DoctorTieneEspecialidades".id;
            public       postgres    false    220            �            1259    49862    practicasMedicas    TABLE     s   CREATE TABLE public."practicasMedicas" (
    codigo integer NOT NULL,
    nombre character varying(50) NOT NULL
);
 &   DROP TABLE public."practicasMedicas";
       public         postgres    false            �
           2604    57993    CM_brinda_Especialidades id    DEFAULT     �   ALTER TABLE ONLY public."CM_brinda_Especialidades" ALTER COLUMN id SET DEFAULT nextval('public."CM_brinda_Especialidades_id_seq"'::regclass);
 L   ALTER TABLE public."CM_brinda_Especialidades" ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    226    227    227            �
           2604    49834    DoctorTieneEspecialidades id    DEFAULT     �   ALTER TABLE ONLY public."DoctorTieneEspecialidades" ALTER COLUMN id SET DEFAULT nextval('public.doctores_doctortieneespecialidad_id_seq'::regclass);
 M   ALTER TABLE public."DoctorTieneEspecialidades" ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    220    221    221            �
           2604    41626    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    202    203    203            �
           2604    41636    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    205    204    205            �
           2604    41618    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    201    200    201            �
           2604    41644    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    206    207    207            �
           2604    41654    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    208    209    209            �
           2604    41662    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    210    211    211            �
           2604    41722    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    212    213    213            �
           2604    41608    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    199    198    199            �
           2604    41597    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public       postgres    false    196    197    197            �          0    49788    Beneficiarios 
   TABLE DATA               s   COPY public."Beneficiarios" ("tipoDNI", dni, nombre, apellidos, afiliado, "nroAfiliado", localidad_id) FROM stdin;
    public       postgres    false    216   <�       �          0    57990    CM_brinda_Especialidades 
   TABLE DATA               ^   COPY public."CM_brinda_Especialidades" (id, "centroMedico_id", especialidades_id) FROM stdin;
    public       postgres    false    227   �       �          0    49801    Centros médicos 
   TABLE DATA               y   COPY public."Centros médicos" ("cuitCM", "razonSocial", domicilio, telefono, horario, e_mail, localidad_id) FROM stdin;
    public       postgres    false    217   ��       �          0    49853    Diagnostico 
   TABLE DATA               7   COPY public."Diagnostico" (codigo, nombre) FROM stdin;
    public       postgres    false    222   ��       �          0    49831    DoctorTieneEspecialidades 
   TABLE DATA               ^   COPY public."DoctorTieneEspecialidades" (id, horario, doctor_id, especialidad_id) FROM stdin;
    public       postgres    false    221   ��       �          0    49816    Doctores 
   TABLE DATA               {   COPY public."Doctores" ("matriculaDoc", cuit, nombre, apellidos, telefono, domicilio, email, "convenioOSECAC") FROM stdin;
    public       postgres    false    218   �       �          0    49821    Especialidades 
   TABLE DATA               Q   COPY public."Especialidades" ("idEspecialidad", nombre, descripcion) FROM stdin;
    public       postgres    false    219   7�       �          0    49783    Localidades 
   TABLE DATA               =   COPY public."Localidades" (codigopostal, nombre) FROM stdin;
    public       postgres    false    215   T�       �          0    49870    PedidosAmbulatorios 
   TABLE DATA               [   COPY public."PedidosAmbulatorios" ("idPedido", fecha_ingreso, beneficiario_id) FROM stdin;
    public       postgres    false    224   ?�       �          0    49877    PracticasDelPedido 
   TABLE DATA               �   COPY public."PracticasDelPedido" (fecha_prescripcion, autorizado, "importeCoseguro", observaciones, diagnosticos_id, doctores_id, practicas_id, pedido_ambulatorio_ptr_id) FROM stdin;
    public       postgres    false    225   \�       �          0    41623 
   auth_group 
   TABLE DATA               .   COPY public.auth_group (id, name) FROM stdin;
    public       postgres    false    203   y�       �          0    41633    auth_group_permissions 
   TABLE DATA               M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public       postgres    false    205   ��       �          0    41615    auth_permission 
   TABLE DATA               N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public       postgres    false    201   ��       �          0    41641 	   auth_user 
   TABLE DATA               �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public       postgres    false    207   ��       �          0    41651    auth_user_groups 
   TABLE DATA               A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public       postgres    false    209   ��       �          0    41659    auth_user_user_permissions 
   TABLE DATA               P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public       postgres    false    211   ��       �          0    41719    django_admin_log 
   TABLE DATA               �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public       postgres    false    213   �       �          0    41605    django_content_type 
   TABLE DATA               C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public       postgres    false    199   E�       �          0    41594    django_migrations 
   TABLE DATA               C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public       postgres    false    197   2�       �          0    41750    django_session 
   TABLE DATA               P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public       postgres    false    214   C�       �          0    49862    practicasMedicas 
   TABLE DATA               <   COPY public."practicasMedicas" (codigo, nombre) FROM stdin;
    public       postgres    false    223   ��                  0    0    CM_brinda_Especialidades_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public."CM_brinda_Especialidades_id_seq"', 1, false);
            public       postgres    false    226                       0    0    auth_group_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);
            public       postgres    false    202                       0    0    auth_group_permissions_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 3, true);
            public       postgres    false    204                       0    0    auth_permission_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_permission_id_seq', 68, true);
            public       postgres    false    200                       0    0    auth_user_groups_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, true);
            public       postgres    false    208                       0    0    auth_user_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.auth_user_id_seq', 2, true);
            public       postgres    false    206                       0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 2, true);
            public       postgres    false    210                       0    0    django_admin_log_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 6, true);
            public       postgres    false    212                       0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 17, true);
            public       postgres    false    198                       0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 38, true);
            public       postgres    false    196                       0    0 '   doctores_doctortieneespecialidad_id_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('public.doctores_doctortieneespecialidad_id_seq', 1, false);
            public       postgres    false    220            N           2606    57995 6   CM_brinda_Especialidades CM_brinda_Especialidades_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public."CM_brinda_Especialidades"
    ADD CONSTRAINT "CM_brinda_Especialidades_pkey" PRIMARY KEY (id);
 d   ALTER TABLE ONLY public."CM_brinda_Especialidades" DROP CONSTRAINT "CM_brinda_Especialidades_pkey";
       public         postgres    false    227            <           2606    57986 6   Diagnostico Diagnostico_codigo_Diagnostico_6ecab46e_pk 
   CONSTRAINT     |   ALTER TABLE ONLY public."Diagnostico"
    ADD CONSTRAINT "Diagnostico_codigo_Diagnostico_6ecab46e_pk" PRIMARY KEY (codigo);
 d   ALTER TABLE ONLY public."Diagnostico" DROP CONSTRAINT "Diagnostico_codigo_Diagnostico_6ecab46e_pk";
       public         postgres    false    222            >           2606    57984 8   Diagnostico Diagnostico_codigo_Diagnostico_6ecab46e_uniq 
   CONSTRAINT     y   ALTER TABLE ONLY public."Diagnostico"
    ADD CONSTRAINT "Diagnostico_codigo_Diagnostico_6ecab46e_uniq" UNIQUE (codigo);
 f   ALTER TABLE ONLY public."Diagnostico" DROP CONSTRAINT "Diagnostico_codigo_Diagnostico_6ecab46e_uniq";
       public         postgres    false    222            E           2606    57977 :   PracticasDelPedido PedidoAmbulatorio_tiene_prácticas_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."PracticasDelPedido"
    ADD CONSTRAINT "PedidoAmbulatorio_tiene_prácticas_pkey" PRIMARY KEY (pedido_ambulatorio_ptr_id);
 h   ALTER TABLE ONLY public."PracticasDelPedido" DROP CONSTRAINT "PedidoAmbulatorio_tiene_prácticas_pkey";
       public         postgres    false    225                       2606    41748    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public         postgres    false    203                       2606    41675 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public         postgres    false    205    205                       2606    41638 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public         postgres    false    205                       2606    41628    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public         postgres    false    203            �
           2606    41666 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public         postgres    false    201    201                        2606    41620 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public         postgres    false    201                       2606    41656 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public         postgres    false    209                       2606    41690 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public         postgres    false    209    209                       2606    41646    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public         postgres    false    207                       2606    41664 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public         postgres    false    211                       2606    41704 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public         postgres    false    211    211                       2606    41742     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public         postgres    false    207            )           2606    49792 ,   Beneficiarios beneficiario_beneficiario_pkey 
   CONSTRAINT     m   ALTER TABLE ONLY public."Beneficiarios"
    ADD CONSTRAINT beneficiario_beneficiario_pkey PRIMARY KEY (dni);
 X   ALTER TABLE ONLY public."Beneficiarios" DROP CONSTRAINT beneficiario_beneficiario_pkey;
       public         postgres    false    216            +           2606    49794 A   Beneficiarios beneficiario_beneficiario_tipoDNI_dni_63a4c255_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public."Beneficiarios"
    ADD CONSTRAINT "beneficiario_beneficiario_tipoDNI_dni_63a4c255_uniq" UNIQUE ("tipoDNI", dni);
 o   ALTER TABLE ONLY public."Beneficiarios" DROP CONSTRAINT "beneficiario_beneficiario_tipoDNI_dni_63a4c255_uniq";
       public         postgres    false    216    216            /           2606    49808 0   Centros médicos centro_medico_centromedico_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public."Centros médicos"
    ADD CONSTRAINT centro_medico_centromedico_pkey PRIMARY KEY ("cuitCM");
 \   ALTER TABLE ONLY public."Centros médicos" DROP CONSTRAINT centro_medico_centromedico_pkey;
       public         postgres    false    217                       2606    41728 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public         postgres    false    213            �
           2606    41612 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public         postgres    false    199    199            �
           2606    41610 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public         postgres    false    199            �
           2606    41602 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public         postgres    false    197            #           2606    41757 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public         postgres    false    214            2           2606    49820    Doctores doctores_doctor_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public."Doctores"
    ADD CONSTRAINT doctores_doctor_pkey PRIMARY KEY (cuit);
 I   ALTER TABLE ONLY public."Doctores" DROP CONSTRAINT doctores_doctor_pkey;
       public         postgres    false    218            9           2606    49836 ?   DoctorTieneEspecialidades doctores_doctortieneespecialidad_pkey 
   CONSTRAINT        ALTER TABLE ONLY public."DoctorTieneEspecialidades"
    ADD CONSTRAINT doctores_doctortieneespecialidad_pkey PRIMARY KEY (id);
 k   ALTER TABLE ONLY public."DoctorTieneEspecialidades" DROP CONSTRAINT doctores_doctortieneespecialidad_pkey;
       public         postgres    false    221            4           2606    49828 )   Especialidades doctores_especialidad_pkey 
   CONSTRAINT     w   ALTER TABLE ONLY public."Especialidades"
    ADD CONSTRAINT doctores_especialidad_pkey PRIMARY KEY ("idEspecialidad");
 U   ALTER TABLE ONLY public."Especialidades" DROP CONSTRAINT doctores_especialidad_pkey;
       public         postgres    false    219            &           2606    49787 -   Localidades localidad_atencion_localidad_pkey 
   CONSTRAINT     w   ALTER TABLE ONLY public."Localidades"
    ADD CONSTRAINT localidad_atencion_localidad_pkey PRIMARY KEY (codigopostal);
 Y   ALTER TABLE ONLY public."Localidades" DROP CONSTRAINT localidad_atencion_localidad_pkey;
       public         postgres    false    215            C           2606    49874 >   PedidosAmbulatorios pedido_ambulatorio_pedido_ambulatorio_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."PedidosAmbulatorios"
    ADD CONSTRAINT pedido_ambulatorio_pedido_ambulatorio_pkey PRIMARY KEY ("idPedido");
 j   ALTER TABLE ONLY public."PedidosAmbulatorios" DROP CONSTRAINT pedido_ambulatorio_pedido_ambulatorio_pkey;
       public         postgres    false    224            @           2606    49869 8   practicasMedicas pedido_ambulatorio_practica_medica_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public."practicasMedicas"
    ADD CONSTRAINT pedido_ambulatorio_practica_medica_pkey PRIMARY KEY (codigo);
 d   ALTER TABLE ONLY public."practicasMedicas" DROP CONSTRAINT pedido_ambulatorio_practica_medica_pkey;
       public         postgres    false    223            J           1259    58006 1   CM_brinda_Especialidades_centroMedico_id_745ba050    INDEX     �   CREATE INDEX "CM_brinda_Especialidades_centroMedico_id_745ba050" ON public."CM_brinda_Especialidades" USING btree ("centroMedico_id");
 G   DROP INDEX public."CM_brinda_Especialidades_centroMedico_id_745ba050";
       public         postgres    false    227            K           1259    58007 6   CM_brinda_Especialidades_centroMedico_id_745ba050_like    INDEX     �   CREATE INDEX "CM_brinda_Especialidades_centroMedico_id_745ba050_like" ON public."CM_brinda_Especialidades" USING btree ("centroMedico_id" varchar_pattern_ops);
 L   DROP INDEX public."CM_brinda_Especialidades_centroMedico_id_745ba050_like";
       public         postgres    false    227            L           1259    58008 3   CM_brinda_Especialidades_especialidades_id_70545102    INDEX     �   CREATE INDEX "CM_brinda_Especialidades_especialidades_id_70545102" ON public."CM_brinda_Especialidades" USING btree (especialidades_id);
 I   DROP INDEX public."CM_brinda_Especialidades_especialidades_id_70545102";
       public         postgres    false    227            :           1259    57987 ,   Diagnostico_codigo_Diagnostico_6ecab46e_like    INDEX     ~   CREATE INDEX "Diagnostico_codigo_Diagnostico_6ecab46e_like" ON public."Diagnostico" USING btree (codigo varchar_pattern_ops);
 B   DROP INDEX public."Diagnostico_codigo_Diagnostico_6ecab46e_like";
       public         postgres    false    222                       1259    41749    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public         postgres    false    203                       1259    41686 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public         postgres    false    205            	           1259    41687 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public         postgres    false    205            �
           1259    41672 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public         postgres    false    201                       1259    41702 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public         postgres    false    209                       1259    41701 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public         postgres    false    209                       1259    41716 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public         postgres    false    211                       1259    41715 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public         postgres    false    211                       1259    41743     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public         postgres    false    207            '           1259    49800 /   beneficiario_beneficiario_localidad_id_08acaf9e    INDEX     s   CREATE INDEX beneficiario_beneficiario_localidad_id_08acaf9e ON public."Beneficiarios" USING btree (localidad_id);
 C   DROP INDEX public.beneficiario_beneficiario_localidad_id_08acaf9e;
       public         postgres    false    216            ,           1259    49814 /   centro_medico_centromedico_cuitCM_6c0ed64b_like    INDEX     �   CREATE INDEX "centro_medico_centromedico_cuitCM_6c0ed64b_like" ON public."Centros médicos" USING btree ("cuitCM" varchar_pattern_ops);
 E   DROP INDEX public."centro_medico_centromedico_cuitCM_6c0ed64b_like";
       public         postgres    false    217            -           1259    49815 0   centro_medico_centromedico_localidad_id_c19ffb27    INDEX     w   CREATE INDEX centro_medico_centromedico_localidad_id_c19ffb27 ON public."Centros médicos" USING btree (localidad_id);
 D   DROP INDEX public.centro_medico_centromedico_localidad_id_c19ffb27;
       public         postgres    false    217                       1259    41739 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public         postgres    false    213                        1259    41740 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public         postgres    false    213            !           1259    41759 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public         postgres    false    214            $           1259    41758 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public         postgres    false    214            0           1259    49837 "   doctores_doctor_cuit_364e3bf4_like    INDEX     m   CREATE INDEX doctores_doctor_cuit_364e3bf4_like ON public."Doctores" USING btree (cuit varchar_pattern_ops);
 6   DROP INDEX public.doctores_doctor_cuit_364e3bf4_like;
       public         postgres    false    218            5           1259    49848 3   doctores_doctortieneespecialidad_doctor_id_654ca4c4    INDEX     �   CREATE INDEX doctores_doctortieneespecialidad_doctor_id_654ca4c4 ON public."DoctorTieneEspecialidades" USING btree (doctor_id);
 G   DROP INDEX public.doctores_doctortieneespecialidad_doctor_id_654ca4c4;
       public         postgres    false    221            6           1259    49849 8   doctores_doctortieneespecialidad_doctor_id_654ca4c4_like    INDEX     �   CREATE INDEX doctores_doctortieneespecialidad_doctor_id_654ca4c4_like ON public."DoctorTieneEspecialidades" USING btree (doctor_id varchar_pattern_ops);
 L   DROP INDEX public.doctores_doctortieneespecialidad_doctor_id_654ca4c4_like;
       public         postgres    false    221            7           1259    49850 9   doctores_doctortieneespecialidad_especialidad_id_6b19d44a    INDEX     �   CREATE INDEX doctores_doctortieneespecialidad_especialidad_id_6b19d44a ON public."DoctorTieneEspecialidades" USING btree (especialidad_id);
 M   DROP INDEX public.doctores_doctortieneespecialidad_especialidad_id_6b19d44a;
       public         postgres    false    221            F           1259    49907 >   pedido_ambulatorio_pa_tiene_practicas_diagnosticos_id_d5b86a04    INDEX     �   CREATE INDEX pedido_ambulatorio_pa_tiene_practicas_diagnosticos_id_d5b86a04 ON public."PracticasDelPedido" USING btree (diagnosticos_id);
 R   DROP INDEX public.pedido_ambulatorio_pa_tiene_practicas_diagnosticos_id_d5b86a04;
       public         postgres    false    225            G           1259    49908 :   pedido_ambulatorio_pa_tiene_practicas_doctores_id_b0d66ba7    INDEX     �   CREATE INDEX pedido_ambulatorio_pa_tiene_practicas_doctores_id_b0d66ba7 ON public."PracticasDelPedido" USING btree (doctores_id);
 N   DROP INDEX public.pedido_ambulatorio_pa_tiene_practicas_doctores_id_b0d66ba7;
       public         postgres    false    225            H           1259    49909 ?   pedido_ambulatorio_pa_tiene_practicas_doctores_id_b0d66ba7_like    INDEX     �   CREATE INDEX pedido_ambulatorio_pa_tiene_practicas_doctores_id_b0d66ba7_like ON public."PracticasDelPedido" USING btree (doctores_id varchar_pattern_ops);
 S   DROP INDEX public.pedido_ambulatorio_pa_tiene_practicas_doctores_id_b0d66ba7_like;
       public         postgres    false    225            I           1259    49910 ;   pedido_ambulatorio_pa_tiene_practicas_practicas_id_be864776    INDEX     �   CREATE INDEX pedido_ambulatorio_pa_tiene_practicas_practicas_id_be864776 ON public."PracticasDelPedido" USING btree (practicas_id);
 O   DROP INDEX public.pedido_ambulatorio_pa_tiene_practicas_practicas_id_be864776;
       public         postgres    false    225            A           1259    49891 >   pedido_ambulatorio_pedido_ambulatorio_beneficiario_id_0515eff7    INDEX     �   CREATE INDEX pedido_ambulatorio_pedido_ambulatorio_beneficiario_id_0515eff7 ON public."PedidosAmbulatorios" USING btree (beneficiario_id);
 R   DROP INDEX public.pedido_ambulatorio_pedido_ambulatorio_beneficiario_id_0515eff7;
       public         postgres    false    224            `           2606    57996 S   CM_brinda_Especialidades CM_brinda_Especialid_centroMedico_id_745ba050_fk_Centros m    FK CONSTRAINT     �   ALTER TABLE ONLY public."CM_brinda_Especialidades"
    ADD CONSTRAINT "CM_brinda_Especialid_centroMedico_id_745ba050_fk_Centros m" FOREIGN KEY ("centroMedico_id") REFERENCES public."Centros médicos"("cuitCM") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."CM_brinda_Especialidades" DROP CONSTRAINT "CM_brinda_Especialid_centroMedico_id_745ba050_fk_Centros m";
       public       postgres    false    2863    227    217            a           2606    58001 U   CM_brinda_Especialidades CM_brinda_Especialid_especialidades_id_70545102_fk_Especiali    FK CONSTRAINT     �   ALTER TABLE ONLY public."CM_brinda_Especialidades"
    ADD CONSTRAINT "CM_brinda_Especialid_especialidades_id_70545102_fk_Especiali" FOREIGN KEY (especialidades_id) REFERENCES public."Especialidades"("idEspecialidad") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."CM_brinda_Especialidades" DROP CONSTRAINT "CM_brinda_Especialid_especialidades_id_70545102_fk_Especiali";
       public       postgres    false    2868    227    219            _           2606    57978 R   PracticasDelPedido PedidoAmbulatorio_ti_pedido_ambulatorio_p_1b35dc4a_fk_Pedidos A    FK CONSTRAINT     �   ALTER TABLE ONLY public."PracticasDelPedido"
    ADD CONSTRAINT "PedidoAmbulatorio_ti_pedido_ambulatorio_p_1b35dc4a_fk_Pedidos A" FOREIGN KEY (pedido_ambulatorio_ptr_id) REFERENCES public."PedidosAmbulatorios"("idPedido") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."PracticasDelPedido" DROP CONSTRAINT "PedidoAmbulatorio_ti_pedido_ambulatorio_p_1b35dc4a_fk_Pedidos A";
       public       postgres    false    2883    224    225            Q           2606    41681 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public       postgres    false    201    2816    205            P           2606    41676 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public       postgres    false    203    205    2821            O           2606    41667 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public       postgres    false    199    201    2811            S           2606    41696 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public       postgres    false    2821    209    203            R           2606    41691 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public       postgres    false    209    2829    207            U           2606    41710 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public       postgres    false    211    201    2816            T           2606    41705 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public       postgres    false    211    2829    207            X           2606    49795 E   Beneficiarios beneficiario_benefic_localidad_id_08acaf9e_fk_localidad    FK CONSTRAINT     �   ALTER TABLE ONLY public."Beneficiarios"
    ADD CONSTRAINT beneficiario_benefic_localidad_id_08acaf9e_fk_localidad FOREIGN KEY (localidad_id) REFERENCES public."Localidades"(codigopostal) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public."Beneficiarios" DROP CONSTRAINT beneficiario_benefic_localidad_id_08acaf9e_fk_localidad;
       public       postgres    false    215    216    2854            Y           2606    49809 H   Centros médicos centro_medico_centro_localidad_id_c19ffb27_fk_localidad    FK CONSTRAINT     �   ALTER TABLE ONLY public."Centros médicos"
    ADD CONSTRAINT centro_medico_centro_localidad_id_c19ffb27_fk_localidad FOREIGN KEY (localidad_id) REFERENCES public."Localidades"(codigopostal) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public."Centros médicos" DROP CONSTRAINT centro_medico_centro_localidad_id_c19ffb27_fk_localidad;
       public       postgres    false    2854    215    217            V           2606    41729 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public       postgres    false    2811    199    213            W           2606    41734 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public       postgres    false    213    207    2829            Z           2606    49838 N   DoctorTieneEspecialidades doctores_doctortiene_doctor_id_654ca4c4_fk_doctores_    FK CONSTRAINT     �   ALTER TABLE ONLY public."DoctorTieneEspecialidades"
    ADD CONSTRAINT doctores_doctortiene_doctor_id_654ca4c4_fk_doctores_ FOREIGN KEY (doctor_id) REFERENCES public."Doctores"(cuit) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public."DoctorTieneEspecialidades" DROP CONSTRAINT doctores_doctortiene_doctor_id_654ca4c4_fk_doctores_;
       public       postgres    false    221    2866    218            [           2606    49843 T   DoctorTieneEspecialidades doctores_doctortiene_especialidad_id_6b19d44a_fk_doctores_    FK CONSTRAINT     �   ALTER TABLE ONLY public."DoctorTieneEspecialidades"
    ADD CONSTRAINT doctores_doctortiene_especialidad_id_6b19d44a_fk_doctores_ FOREIGN KEY (especialidad_id) REFERENCES public."Especialidades"("idEspecialidad") DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public."DoctorTieneEspecialidades" DROP CONSTRAINT doctores_doctortiene_especialidad_id_6b19d44a_fk_doctores_;
       public       postgres    false    221    2868    219            \           2606    49886 N   PedidosAmbulatorios pedido_ambulatorio_p_beneficiario_id_0515eff7_fk_beneficia    FK CONSTRAINT     �   ALTER TABLE ONLY public."PedidosAmbulatorios"
    ADD CONSTRAINT pedido_ambulatorio_p_beneficiario_id_0515eff7_fk_beneficia FOREIGN KEY (beneficiario_id) REFERENCES public."Beneficiarios"(dni) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public."PedidosAmbulatorios" DROP CONSTRAINT pedido_ambulatorio_p_beneficiario_id_0515eff7_fk_beneficia;
       public       postgres    false    224    216    2857            ]           2606    49897 I   PracticasDelPedido pedido_ambulatorio_p_doctores_id_b0d66ba7_fk_doctores_    FK CONSTRAINT     �   ALTER TABLE ONLY public."PracticasDelPedido"
    ADD CONSTRAINT pedido_ambulatorio_p_doctores_id_b0d66ba7_fk_doctores_ FOREIGN KEY (doctores_id) REFERENCES public."Doctores"(cuit) DEFERRABLE INITIALLY DEFERRED;
 u   ALTER TABLE ONLY public."PracticasDelPedido" DROP CONSTRAINT pedido_ambulatorio_p_doctores_id_b0d66ba7_fk_doctores_;
       public       postgres    false    218    225    2866            ^           2606    49902 J   PracticasDelPedido pedido_ambulatorio_p_practicas_id_be864776_fk_pedido_am    FK CONSTRAINT     �   ALTER TABLE ONLY public."PracticasDelPedido"
    ADD CONSTRAINT pedido_ambulatorio_p_practicas_id_be864776_fk_pedido_am FOREIGN KEY (practicas_id) REFERENCES public."practicasMedicas"(codigo) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public."PracticasDelPedido" DROP CONSTRAINT pedido_ambulatorio_p_practicas_id_be864776_fk_pedido_am;
       public       postgres    false    225    2880    223            �   3   x�3�46477243�tN,�M���-=�1��3����������̀+F��� ��
F      �      x������ � �      �      x������ � �      �   4  x��T[��0�&����xf7��*cQ�������X�@2$5�UwK��2�i�h6�@5XS�
ԙjG�t7�Qq��j�@��A�f/)Ѩ�.���J���%��IKX;T�Z�!�98��P#�oBu��MHG�܂�����i�6��@~jS�*�g�ƌ�,�8��<��	��&	yeX���R�a�_	'�Z�~�W�{����a��Ua��"M|GG4�oZc�h.~�ĸ�"{�n~X!Gj��Z󥡑X<'z�G�<����[�]��be�5�����Nv(�$56�>��*�t�?h��/�Ȟ��y�/�:��98J�QZn����Y0�W��O�Ֆ�5���pZ���o�.�<Y�5�+f�G�LֱufYYp�ЩW��)2�d��ܴ1=����uD���J�u�UtGܞ�Q(w�˳�Ŗ|���xYO-UYRs8�}tV�?�n6;�kY1�W��;Y��I�o$����7�@�`.2�S�BU~C.#!cN��I��~��W��~�Bux\��&�i����(襘0O�%S,^�j�ڱ���ϓ�j�j)�t"c�a�d���n���M��      �      x������ � �      �      x������ � �      �      x������ � �      �   �   x���N�0�g�)�U���1��	Ai|�	b`AL'����8],�|�l/~q���v��5�w,���Z_�ƃxT�4��.�Y�bN'1
VM���JRP6�E�mԉ��^���3��vE�ҕh_�7���TR�]�5�&uY䣓3��[��dFm��b� ���e����i�pC!�z��f�؇O XB���@H
���U�P6_�1���C�      �      x������ � �      �      x������ � �      �      x�3�p
��s������ �Q      �      x�3�4�46�2Qf\�@�̀+F��� .:Z      �   �  x���[��0���U���B.��F%䀛ZJ iuv_���������<%~��]W<�Ga�e�J�����������a�E��3O�pЅ"x�5��"Tg��^v��Ћ�ŀ<SsDw��P�E���F�������ix����,�5���"�z��A��V< .p�
޳��	l�R������;���#��;���e8�-^����/���hD0�E��R#	�����Q���6�2V׳q�z��&K��A�c�1�0��W��~7��m[�';�آ!Y�tOh4�,�Z���	�9��݊v(^��� �. �B�bŐ�>	���F��i��TR�%�c�tC����m�"+V=�@�b 4�!RE?��d�Ѭ�i;݉��l�hLV��R�q��T�V��D�)��7�U��ŮY�(�����(�?;��������dvb�t��)���>�*v���Z/*qĶ�b���0e�j��a���3#q�.V�VG74�~��O�~�Z��¹KdE֬�3�0��rV�y��{9)���^�,t���Ŷz���/�Y�Ɛ�o>г�����>Гv�S��>��N�Y��y�ڣr3��d��L��<�2	�+��g�c��ec��Ҹή�r�;�]X�YC9R�J��	�ͤB�.�d�JRQ�l`5���ݪ��ĬW{�MV�rR�YG�t�9�۟u�O�?�ڹ�I��t�݌���뇔�?��Y      �   �   x�m�]o�@E��_��tw�]>�&������ib�ʧPS~}imS�v^�L&��TYö�`\&�Gvݡd;CNT�Oõx���C�x2A83����a����63=p��=�C�+�P�~�"���
�)����HJ�.y�+D�������ߠ��d�Ġ�=*����t��y�^�����?ⲋ�o$}�ݶ�7�<tvuk�e��'43���j���F	ӿLcTEus(EN�6QE���J��k㟺/�$I¢]�      �      x�3�4�4����� �Y      �      x�3�4�42�2Q\1z\\\ �y      �     x��λN�0��y
�H���5��D��:�&q�(M�8���;	��
a`;����8�,eY
X),c4�*ei����աt%n_?|��q|� �ĕ�/�Ň�q��#H�o5F
�GS�1�D7��U(��B�C��s�tq�s6ĵ�(dJd|�=�>/��`X'r
H�a$���|���0�P ��.(n����5o�����8�kr����m=��$wgͲwU�c��}����ﾪU��m�1�M$�S,=��Ya(�տb���&I�	L���      �   �   x�}P�n�0;[3�}n�2�Pl5�X����S�m�`7��HQ�a�9�IFʭ�a�pi߮P�Y�%ö3c�����E���E���ڹ�>88���8��2�82V� .^�%̔8�u �.IlR-���i!s�8a�k[Ϋfcec��h�=(�[+�8I�yX&4;�/~�*�p��blQ��ׄ�q̢�R�V�n�+��ϛ�P9'�]I�� ~ �B�*      �     x����n�0���S��<�ϲ�E��"��ڷ��NIҀ��p����1�U];�v�OaȄ���ɤ�b'�N�W)
�
�r�D;�/2+����
'�"3U`V�u���r$a���k��Mw`����ñ�����r�_d(��81���W������My��GWW��"�$	�X��.�����OO|[�"JK"�'�����l���S��0L��z,�|����BC*��f^P�/�X��S�2B���LQ����t�q����1 f��e4�0N�׼�s��tmК���b�ݿ纟퍾�ɴ��$#�O{��Y6���~��}�����<�4^��"���yb����$L�$z�hJ��d��A���}w>mð��fƀ?�آ�O}��}��e��V%)6��ͧ���Nf����ގ���	K ��
�@U(���d���І���˾*J�8�DVM�����jC�5�R���l�U��y[�r�\Rf'�֞�����LY|�Y�F�� �a�2���N80�cqK�L��!�.���7S�䁾�`;��	f�����"-ʮX���r�,����2��H)�"e!�@>+4�T�B�6o���Q�;�7�Ԕ���Y���-õog��p���X���+˾B$B� P�Q��V>�Jw�[_��҇���эy��`Qr �.a��D�[���ea
!�L�4��y`�9z�bi���-M	ŵ���,'��}��-��x��[a��,��6��a��Q�t���_^^����A      �   �  x������0�>ż������,�%��L��F`�-�sG�O?x��bֳ=����w���k�Cu����x6���nu�>�	'$J��D.�Ч�8��n1���,��uh�uR Q-��]��	e]�gN�朧ꠒG�U�ձlꂚʄ���&�Kt�D|���������yΓ_�ȼ�{�'W=Z�є۽��iJ����}�ۅ���Y����Nܮ;�����N���:�7����lcH�u����:���}x3o5C�7��h���|�E�<<��U���������b۪��-�G����N(3��7����qf�M1Ϸ���RL��ݍn{Kl�q:��=��K��h#��H�&�`�C��n��ωZ��.S�a�e��� �/���t�l��)      �      x������ � �     