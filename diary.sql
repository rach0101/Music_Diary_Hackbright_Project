--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: posts; Type: TABLE; Schema: public; Owner: rachelcleak
--

CREATE TABLE public.posts (
    post_id integer NOT NULL,
    user_id integer,
    date timestamp without time zone,
    post_content character varying(200) NOT NULL,
    spotify_id character varying,
    music_title character varying(75),
    music_type character varying(8),
    music_img character varying,
    music_url character varying
);


ALTER TABLE public.posts OWNER TO rachelcleak;

--
-- Name: posts_post_id_seq; Type: SEQUENCE; Schema: public; Owner: rachelcleak
--

CREATE SEQUENCE public.posts_post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.posts_post_id_seq OWNER TO rachelcleak;

--
-- Name: posts_post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rachelcleak
--

ALTER SEQUENCE public.posts_post_id_seq OWNED BY public.posts.post_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: rachelcleak
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(50) NOT NULL,
    password character varying(50) NOT NULL,
    spotify_username character varying(50) NOT NULL,
    token character varying NOT NULL
);


ALTER TABLE public.users OWNER TO rachelcleak;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: rachelcleak
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO rachelcleak;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rachelcleak
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: posts post_id; Type: DEFAULT; Schema: public; Owner: rachelcleak
--

ALTER TABLE ONLY public.posts ALTER COLUMN post_id SET DEFAULT nextval('public.posts_post_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: rachelcleak
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: rachelcleak
--

COPY public.posts (post_id, user_id, date, post_content, spotify_id, music_title, music_type, music_img, music_url) FROM stdin;
1	1	2021-08-24 15:23:48.325686	This song reminds me of good times in San Francisco.	09IStsImFySgyp0pIQdqAc	The Middle	song	https://i.scdn.co/image/ab67616d00004851fbe22d168a743b782a5e856a	https://open.spotify.com/track/09IStsImFySgyp0pIQdqAc
2	1	2021-08-24 15:24:53.306137	great summer song :)	2kAIpGWnlFLQh48iut6Zzq	Free Spirit	song	https://i.scdn.co/image/ab67616d00004851b361ce46dbadbf8a11081b60	https://open.spotify.com/track/2kAIpGWnlFLQh48iut6Zzq
3	1	2021-08-24 15:25:16.457945	one of my favorite songs of all time.	3a1lNhkSLSkpJE4MSHpDu9	Congratulations	song	https://i.scdn.co/image/ab67616d0000485155404f712deb84d0650a4b41	https://open.spotify.com/track/3a1lNhkSLSkpJE4MSHpDu9
4	1	2021-08-24 15:25:47.156181	My new favorite song. I love LANY and Kelsea Ballerini so much.	6OcCk1dbAb7XNHsC098oEM	I Quit Drinking	song	https://i.scdn.co/image/ab67616d00004851b0be5e7275db8b7baa1ef779	https://open.spotify.com/track/6OcCk1dbAb7XNHsC098oEM
5	1	2021-08-24 15:27:55.84578	Great acoustic edm. I like the lyrics "our disco ball's my kitchen light."	3Dkvp3L4w0uJFYfIPa8E9H	ILYSB - STRIPPED	song	https://i.scdn.co/image/ab67616d0000485183e2fb0089b24f193246942f	https://open.spotify.com/track/3Dkvp3L4w0uJFYfIPa8E9H
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: rachelcleak
--

COPY public.users (user_id, username, password, spotify_username, token) FROM stdin;
1	rach0101	1234test	rachie.luvs.music	akdjiosfajjesjiefjefijoijio
2	balloonicorn	test1234	iamcute21	aaabbbcccdddeeefff
3				
4	test	test	test	test
6	josh	joshrules	djfdjoidfj;fdjiofvioj	jknfvdufvdjfdvjio
7	rachel	1234	1234	1234
8	sean	sean	sean	sean
\.


--
-- Name: posts_post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rachelcleak
--

SELECT pg_catalog.setval('public.posts_post_id_seq', 5, true);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rachelcleak
--

SELECT pg_catalog.setval('public.users_user_id_seq', 8, true);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: rachelcleak
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (post_id);


--
-- Name: posts posts_post_content_key; Type: CONSTRAINT; Schema: public; Owner: rachelcleak
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_post_content_key UNIQUE (post_content);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: rachelcleak
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: users users_spotify_username_key; Type: CONSTRAINT; Schema: public; Owner: rachelcleak
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_spotify_username_key UNIQUE (spotify_username);


--
-- Name: users users_token_key; Type: CONSTRAINT; Schema: public; Owner: rachelcleak
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_token_key UNIQUE (token);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: rachelcleak
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: posts posts_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: rachelcleak
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

