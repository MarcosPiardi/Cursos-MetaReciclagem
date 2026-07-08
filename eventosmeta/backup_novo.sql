--
-- PostgreSQL database dump
--

\restrict v9zDbaVjQrlgGcqirPD65WFwahpUrJTpsUzOtH643b8IPpB8FHZzWvw7HdygrLl

-- Dumped from database version 15.18
-- Dumped by pg_dump version 15.18

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

ALTER TABLE IF EXISTS ONLY public.selecao_inscricaocriterioatendido DROP CONSTRAINT IF EXISTS selecao_inscricaocri_inscricao_id_f4596be5_fk_selecao_i;
ALTER TABLE IF EXISTS ONLY public.selecao_inscricaocriterioatendido DROP CONSTRAINT IF EXISTS selecao_inscricaocri_criterio_id_92a1333d_fk_eventos_c;
ALTER TABLE IF EXISTS ONLY public.selecao_inscricao DROP CONSTRAINT IF EXISTS selecao_inscricao_status_id_1747a6a8_fk_selecao_s;
ALTER TABLE IF EXISTS ONLY public.selecao_inscricao DROP CONSTRAINT IF EXISTS selecao_inscricao_interessado_id_c7990ace_fk_interessa;
ALTER TABLE IF EXISTS ONLY public.selecao_inscricao DROP CONSTRAINT IF EXISTS selecao_inscricao_evento_id_69022fc4_fk_eventos_evento_id;
ALTER TABLE IF EXISTS ONLY public.selecao_classificacao DROP CONSTRAINT IF EXISTS selecao_classificaca_inscricao_id_32f20847_fk_selecao_i;
ALTER TABLE IF EXISTS ONLY public.interessados_solicitacaoexclusao DROP CONSTRAINT IF EXISTS interessados_solicit_interessado_id_72cb2d83_fk_interessa;
ALTER TABLE IF EXISTS ONLY public.interessados_solicitacaoexclusao DROP CONSTRAINT IF EXISTS interessados_solicit_analisado_por_id_a4448b09_fk_accounts_;
ALTER TABLE IF EXISTS ONLY public.interessados_passwordresettoken DROP CONSTRAINT IF EXISTS interessados_passwor_interessado_id_6d208345_fk_interessa;
ALTER TABLE IF EXISTS ONLY public.interessados_interessado DROP CONSTRAINT IF EXISTS interessados_interes_sexo_id_d912f7e0_fk_interessa;
ALTER TABLE IF EXISTS ONLY public.interessados_interessado DROP CONSTRAINT IF EXISTS interessados_interes_fototipo_id_1bd82591_fk_interessa;
ALTER TABLE IF EXISTS ONLY public.eventos_turma DROP CONSTRAINT IF EXISTS eventos_turma_evento_id_63fb57f5_fk_eventos_evento_id;
ALTER TABLE IF EXISTS ONLY public.eventos_horario DROP CONSTRAINT IF EXISTS eventos_horario_turma_id_29c0bdff_fk_eventos_turma_id;
ALTER TABLE IF EXISTS ONLY public.eventos_eventocriterio DROP CONSTRAINT IF EXISTS eventos_eventocriterio_evento_id_5f07f643_fk_eventos_evento_id;
ALTER TABLE IF EXISTS ONLY public.eventos_eventocriterio DROP CONSTRAINT IF EXISTS eventos_eventocriter_criterio_id_7e3b9bd4_fk_eventos_c;
ALTER TABLE IF EXISTS ONLY public.eventos_evento DROP CONSTRAINT IF EXISTS eventos_evento_status_id_412ac246_fk_eventos_status_id;
ALTER TABLE IF EXISTS ONLY public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_user_id_c564eba6_fk_accounts_usuario_id;
ALTER TABLE IF EXISTS ONLY public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_content_type_id_c4bce8eb_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.axes_accessattemptexpiration DROP CONSTRAINT IF EXISTS axes_accessattemptex_access_attempt_id_6b73a47a_fk_axes_acce;
ALTER TABLE IF EXISTS ONLY public.auth_permission DROP CONSTRAINT IF EXISTS auth_permission_content_type_id_2f476e4b_fk_django_co;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario_user_permissions DROP CONSTRAINT IF EXISTS accounts_usuario_use_usuario_id_d048ad71_fk_accounts_;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario_user_permissions DROP CONSTRAINT IF EXISTS accounts_usuario_use_permission_id_3de42c14_fk_auth_perm;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario_groups DROP CONSTRAINT IF EXISTS accounts_usuario_groups_group_id_81d91a41_fk_auth_group_id;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario_groups DROP CONSTRAINT IF EXISTS accounts_usuario_gro_usuario_id_8eb16911_fk_accounts_;
ALTER TABLE IF EXISTS ONLY public.academico_matricula DROP CONSTRAINT IF EXISTS academico_matricula_turma_id_ada4fc93_fk_eventos_turma_id;
ALTER TABLE IF EXISTS ONLY public.academico_matricula DROP CONSTRAINT IF EXISTS academico_matricula_status_id_c0fa5b2c_fk_academico;
ALTER TABLE IF EXISTS ONLY public.academico_matricula DROP CONSTRAINT IF EXISTS academico_matricula_interessado_id_27c13dae_fk_interessa;
ALTER TABLE IF EXISTS ONLY public.academico_matricula DROP CONSTRAINT IF EXISTS academico_matricula_inscricao_id_a95f8468_fk_selecao_i;
ALTER TABLE IF EXISTS ONLY public.academico_avaliacao DROP CONSTRAINT IF EXISTS academico_avaliacao_matricula_id_0125d759_fk_academico;
DROP INDEX IF EXISTS public.selecao_statusinscricao_nome_7e620433_like;
DROP INDEX IF EXISTS public.selecao_inscricaocriterioatendido_inscricao_id_f4596be5;
DROP INDEX IF EXISTS public.selecao_inscricaocriterioatendido_criterio_id_92a1333d;
DROP INDEX IF EXISTS public.selecao_inscricao_status_id_1747a6a8;
DROP INDEX IF EXISTS public.selecao_inscricao_interessado_id_c7990ace;
DROP INDEX IF EXISTS public.selecao_inscricao_evento_id_69022fc4;
DROP INDEX IF EXISTS public.interessados_solicitacaoexclusao_interessado_id_72cb2d83;
DROP INDEX IF EXISTS public.interessados_solicitacaoexclusao_analisado_por_id_a4448b09;
DROP INDEX IF EXISTS public.interessados_sexo_nome_c6c8ae4e_like;
DROP INDEX IF EXISTS public.interessados_passwordresettoken_token_c8a8033f_like;
DROP INDEX IF EXISTS public.interessados_passwordresettoken_interessado_id_6d208345;
DROP INDEX IF EXISTS public.interessados_interessado_sexo_id_d912f7e0;
DROP INDEX IF EXISTS public.interessados_interessado_fototipo_id_1bd82591;
DROP INDEX IF EXISTS public.interessados_interessado_email_004f6a1a_like;
DROP INDEX IF EXISTS public.interessados_interessado_cpf_hash_0c279a5c_like;
DROP INDEX IF EXISTS public.interessados_interessado_cpf_b91198ed_like;
DROP INDEX IF EXISTS public.eventos_turma_evento_id_63fb57f5;
DROP INDEX IF EXISTS public.eventos_status_nome_7b0c99ed_like;
DROP INDEX IF EXISTS public.eventos_horario_turma_id_29c0bdff;
DROP INDEX IF EXISTS public.eventos_eventocriterio_evento_id_5f07f643;
DROP INDEX IF EXISTS public.eventos_eventocriterio_criterio_id_7e3b9bd4;
DROP INDEX IF EXISTS public.eventos_evento_status_id_412ac246;
DROP INDEX IF EXISTS public.eventos_criterio_codigo_b06552c8_like;
DROP INDEX IF EXISTS public.django_session_session_key_c0390e0f_like;
DROP INDEX IF EXISTS public.django_session_expire_date_a5c62663;
DROP INDEX IF EXISTS public.django_admin_log_user_id_c564eba6;
DROP INDEX IF EXISTS public.django_admin_log_content_type_id_c4bce8eb;
DROP INDEX IF EXISTS public.axes_accesslog_username_df93064b_like;
DROP INDEX IF EXISTS public.axes_accesslog_username_df93064b;
DROP INDEX IF EXISTS public.axes_accesslog_user_agent_0e659004_like;
DROP INDEX IF EXISTS public.axes_accesslog_user_agent_0e659004;
DROP INDEX IF EXISTS public.axes_accesslog_ip_address_86b417e5;
DROP INDEX IF EXISTS public.axes_accessfailurelog_username_a8b7e8a4_like;
DROP INDEX IF EXISTS public.axes_accessfailurelog_username_a8b7e8a4;
DROP INDEX IF EXISTS public.axes_accessfailurelog_user_agent_ea145dda_like;
DROP INDEX IF EXISTS public.axes_accessfailurelog_user_agent_ea145dda;
DROP INDEX IF EXISTS public.axes_accessfailurelog_ip_address_2e9f5a7f;
DROP INDEX IF EXISTS public.axes_accessattempt_username_3f2d4ca0_like;
DROP INDEX IF EXISTS public.axes_accessattempt_username_3f2d4ca0;
DROP INDEX IF EXISTS public.axes_accessattempt_user_agent_ad89678b_like;
DROP INDEX IF EXISTS public.axes_accessattempt_user_agent_ad89678b;
DROP INDEX IF EXISTS public.axes_accessattempt_ip_address_10922d9c;
DROP INDEX IF EXISTS public.auth_permission_content_type_id_2f476e4b;
DROP INDEX IF EXISTS public.auth_group_permissions_permission_id_84c5c92e;
DROP INDEX IF EXISTS public.auth_group_permissions_group_id_b120cbf9;
DROP INDEX IF EXISTS public.auth_group_name_a6ea08ec_like;
DROP INDEX IF EXISTS public.accounts_usuario_username_c366c69f_like;
DROP INDEX IF EXISTS public.accounts_usuario_user_permissions_usuario_id_d048ad71;
DROP INDEX IF EXISTS public.accounts_usuario_user_permissions_permission_id_3de42c14;
DROP INDEX IF EXISTS public.accounts_usuario_groups_usuario_id_8eb16911;
DROP INDEX IF EXISTS public.accounts_usuario_groups_group_id_81d91a41;
DROP INDEX IF EXISTS public.accounts_usuario_email_19c7414e_like;
DROP INDEX IF EXISTS public.accounts_usuario_cpf_88f87c69_like;
DROP INDEX IF EXISTS public.academico_statusmatricula_nome_f1319f70_like;
DROP INDEX IF EXISTS public.academico_matricula_turma_id_ada4fc93;
DROP INDEX IF EXISTS public.academico_matricula_status_id_c0fa5b2c;
DROP INDEX IF EXISTS public.academico_matricula_numero_matricula_63207837_like;
DROP INDEX IF EXISTS public.academico_matricula_interessado_id_27c13dae;
DROP INDEX IF EXISTS public.academico_matricula_inscricao_id_a95f8468;
DROP INDEX IF EXISTS public.academico_m_turma_i_1f9f0d_idx;
DROP INDEX IF EXISTS public.academico_m_numero__4bc01b_idx;
DROP INDEX IF EXISTS public.academico_m_inscric_af84a1_idx;
ALTER TABLE IF EXISTS ONLY public.selecao_statusinscricao DROP CONSTRAINT IF EXISTS selecao_statusinscricao_pkey;
ALTER TABLE IF EXISTS ONLY public.selecao_statusinscricao DROP CONSTRAINT IF EXISTS selecao_statusinscricao_nome_key;
ALTER TABLE IF EXISTS ONLY public.selecao_inscricaocriterioatendido DROP CONSTRAINT IF EXISTS selecao_inscricaocriterioatendido_pkey;
ALTER TABLE IF EXISTS ONLY public.selecao_inscricaocriterioatendido DROP CONSTRAINT IF EXISTS selecao_inscricaocriteri_inscricao_id_criterio_id_c88c00eb_uniq;
ALTER TABLE IF EXISTS ONLY public.selecao_inscricao DROP CONSTRAINT IF EXISTS selecao_inscricao_pkey;
ALTER TABLE IF EXISTS ONLY public.selecao_inscricao DROP CONSTRAINT IF EXISTS selecao_inscricao_interessado_id_evento_id_a51d630a_uniq;
ALTER TABLE IF EXISTS ONLY public.selecao_classificacao DROP CONSTRAINT IF EXISTS selecao_classificacao_pkey;
ALTER TABLE IF EXISTS ONLY public.selecao_classificacao DROP CONSTRAINT IF EXISTS selecao_classificacao_inscricao_id_key;
ALTER TABLE IF EXISTS ONLY public.selecao_classificacao DROP CONSTRAINT IF EXISTS selecao_classificacao_inscricao_id_32f20847_uniq;
ALTER TABLE IF EXISTS ONLY public.interessados_solicitacaoexclusao DROP CONSTRAINT IF EXISTS interessados_solicitacaoexclusao_pkey;
ALTER TABLE IF EXISTS ONLY public.interessados_sexo DROP CONSTRAINT IF EXISTS interessados_sexo_pkey;
ALTER TABLE IF EXISTS ONLY public.interessados_sexo DROP CONSTRAINT IF EXISTS interessados_sexo_nome_c6c8ae4e_uniq;
ALTER TABLE IF EXISTS ONLY public.interessados_passwordresettoken DROP CONSTRAINT IF EXISTS interessados_passwordresettoken_token_key;
ALTER TABLE IF EXISTS ONLY public.interessados_passwordresettoken DROP CONSTRAINT IF EXISTS interessados_passwordresettoken_pkey;
ALTER TABLE IF EXISTS ONLY public.interessados_interessado DROP CONSTRAINT IF EXISTS interessados_interessado_pkey;
ALTER TABLE IF EXISTS ONLY public.interessados_interessado DROP CONSTRAINT IF EXISTS interessados_interessado_email_004f6a1a_uniq;
ALTER TABLE IF EXISTS ONLY public.interessados_interessado DROP CONSTRAINT IF EXISTS interessados_interessado_cpf_key;
ALTER TABLE IF EXISTS ONLY public.interessados_interessado DROP CONSTRAINT IF EXISTS interessados_interessado_cpf_hash_0c279a5c_uniq;
ALTER TABLE IF EXISTS ONLY public.interessados_fototipo DROP CONSTRAINT IF EXISTS interessados_fototipo_pkey;
ALTER TABLE IF EXISTS ONLY public.eventos_turma DROP CONSTRAINT IF EXISTS eventos_turma_pkey;
ALTER TABLE IF EXISTS ONLY public.eventos_turma DROP CONSTRAINT IF EXISTS eventos_turma_evento_id_nome_8d323f73_uniq;
ALTER TABLE IF EXISTS ONLY public.eventos_status DROP CONSTRAINT IF EXISTS eventos_status_pkey;
ALTER TABLE IF EXISTS ONLY public.eventos_status DROP CONSTRAINT IF EXISTS eventos_status_nome_key;
ALTER TABLE IF EXISTS ONLY public.eventos_horario DROP CONSTRAINT IF EXISTS eventos_horario_pkey;
ALTER TABLE IF EXISTS ONLY public.eventos_eventocriterio DROP CONSTRAINT IF EXISTS eventos_eventocriterio_pkey;
ALTER TABLE IF EXISTS ONLY public.eventos_eventocriterio DROP CONSTRAINT IF EXISTS eventos_eventocriterio_evento_id_criterio_id_9ee1bd55_uniq;
ALTER TABLE IF EXISTS ONLY public.eventos_evento DROP CONSTRAINT IF EXISTS eventos_evento_pkey;
ALTER TABLE IF EXISTS ONLY public.eventos_criterio DROP CONSTRAINT IF EXISTS eventos_criterio_pkey;
ALTER TABLE IF EXISTS ONLY public.eventos_criterio DROP CONSTRAINT IF EXISTS eventos_criterio_codigo_key;
ALTER TABLE IF EXISTS ONLY public.django_session DROP CONSTRAINT IF EXISTS django_session_pkey;
ALTER TABLE IF EXISTS ONLY public.django_migrations DROP CONSTRAINT IF EXISTS django_migrations_pkey;
ALTER TABLE IF EXISTS ONLY public.django_content_type DROP CONSTRAINT IF EXISTS django_content_type_pkey;
ALTER TABLE IF EXISTS ONLY public.django_content_type DROP CONSTRAINT IF EXISTS django_content_type_app_label_model_76bd3d3b_uniq;
ALTER TABLE IF EXISTS ONLY public.django_admin_log DROP CONSTRAINT IF EXISTS django_admin_log_pkey;
ALTER TABLE IF EXISTS ONLY public.axes_accesslog DROP CONSTRAINT IF EXISTS axes_accesslog_pkey;
ALTER TABLE IF EXISTS ONLY public.axes_accessfailurelog DROP CONSTRAINT IF EXISTS axes_accessfailurelog_pkey;
ALTER TABLE IF EXISTS ONLY public.axes_accessattemptexpiration DROP CONSTRAINT IF EXISTS axes_accessattemptexpiration_pkey;
ALTER TABLE IF EXISTS ONLY public.axes_accessattempt DROP CONSTRAINT IF EXISTS axes_accessattempt_username_ip_address_user_agent_8ea22282_uniq;
ALTER TABLE IF EXISTS ONLY public.axes_accessattempt DROP CONSTRAINT IF EXISTS axes_accessattempt_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_permission DROP CONSTRAINT IF EXISTS auth_permission_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_permission DROP CONSTRAINT IF EXISTS auth_permission_content_type_id_codename_01ab375a_uniq;
ALTER TABLE IF EXISTS ONLY public.auth_group DROP CONSTRAINT IF EXISTS auth_group_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_pkey;
ALTER TABLE IF EXISTS ONLY public.auth_group_permissions DROP CONSTRAINT IF EXISTS auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
ALTER TABLE IF EXISTS ONLY public.auth_group DROP CONSTRAINT IF EXISTS auth_group_name_key;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario DROP CONSTRAINT IF EXISTS accounts_usuario_username_key;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario_user_permissions DROP CONSTRAINT IF EXISTS accounts_usuario_user_permissions_pkey;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario_user_permissions DROP CONSTRAINT IF EXISTS accounts_usuario_user_pe_usuario_id_permission_id_0065a2ce_uniq;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario DROP CONSTRAINT IF EXISTS accounts_usuario_pkey;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario_groups DROP CONSTRAINT IF EXISTS accounts_usuario_groups_usuario_id_group_id_90f476d3_uniq;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario_groups DROP CONSTRAINT IF EXISTS accounts_usuario_groups_pkey;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario DROP CONSTRAINT IF EXISTS accounts_usuario_email_19c7414e_uniq;
ALTER TABLE IF EXISTS ONLY public.accounts_usuario DROP CONSTRAINT IF EXISTS accounts_usuario_cpf_key;
ALTER TABLE IF EXISTS ONLY public.academico_statusmatricula DROP CONSTRAINT IF EXISTS academico_statusmatricula_pkey;
ALTER TABLE IF EXISTS ONLY public.academico_statusmatricula DROP CONSTRAINT IF EXISTS academico_statusmatricula_nome_key;
ALTER TABLE IF EXISTS ONLY public.academico_matricula DROP CONSTRAINT IF EXISTS academico_matricula_turma_id_interessado_id_51257fc9_uniq;
ALTER TABLE IF EXISTS ONLY public.academico_matricula DROP CONSTRAINT IF EXISTS academico_matricula_pkey;
ALTER TABLE IF EXISTS ONLY public.academico_matricula DROP CONSTRAINT IF EXISTS academico_matricula_numero_matricula_key;
ALTER TABLE IF EXISTS ONLY public.academico_avaliacao DROP CONSTRAINT IF EXISTS academico_avaliacao_pkey;
ALTER TABLE IF EXISTS ONLY public.academico_avaliacao DROP CONSTRAINT IF EXISTS academico_avaliacao_matricula_id_key;
DROP TABLE IF EXISTS public.selecao_statusinscricao;
DROP TABLE IF EXISTS public.selecao_inscricaocriterioatendido;
DROP TABLE IF EXISTS public.selecao_inscricao;
DROP TABLE IF EXISTS public.selecao_classificacao;
DROP TABLE IF EXISTS public.interessados_solicitacaoexclusao;
DROP TABLE IF EXISTS public.interessados_sexo;
DROP TABLE IF EXISTS public.interessados_passwordresettoken;
DROP TABLE IF EXISTS public.interessados_interessado;
DROP TABLE IF EXISTS public.interessados_fototipo;
DROP TABLE IF EXISTS public.eventos_turma;
DROP TABLE IF EXISTS public.eventos_status;
DROP TABLE IF EXISTS public.eventos_horario;
DROP TABLE IF EXISTS public.eventos_eventocriterio;
DROP TABLE IF EXISTS public.eventos_evento;
DROP TABLE IF EXISTS public.eventos_criterio;
DROP TABLE IF EXISTS public.django_session;
DROP TABLE IF EXISTS public.django_migrations;
DROP TABLE IF EXISTS public.django_content_type;
DROP TABLE IF EXISTS public.django_admin_log;
DROP TABLE IF EXISTS public.axes_accesslog;
DROP TABLE IF EXISTS public.axes_accessfailurelog;
DROP TABLE IF EXISTS public.axes_accessattemptexpiration;
DROP TABLE IF EXISTS public.axes_accessattempt;
DROP TABLE IF EXISTS public.auth_permission;
DROP TABLE IF EXISTS public.auth_group_permissions;
DROP TABLE IF EXISTS public.auth_group;
DROP TABLE IF EXISTS public.accounts_usuario_user_permissions;
DROP TABLE IF EXISTS public.accounts_usuario_groups;
DROP TABLE IF EXISTS public.accounts_usuario;
DROP TABLE IF EXISTS public.academico_statusmatricula;
DROP TABLE IF EXISTS public.academico_matricula;
DROP TABLE IF EXISTS public.academico_avaliacao;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: academico_avaliacao; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.academico_avaliacao (
    id bigint NOT NULL,
    nota_final numeric(4,2),
    frequencia numeric(5,2) NOT NULL,
    aprovado boolean NOT NULL,
    observacoes text NOT NULL,
    certificado_emitido boolean NOT NULL,
    data_emissao_certificado date,
    avaliado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL,
    matricula_id bigint NOT NULL
);


ALTER TABLE public.academico_avaliacao OWNER TO metareciclagem_user;

--
-- Name: academico_avaliacao_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.academico_avaliacao ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.academico_avaliacao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: academico_matricula; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.academico_matricula (
    id bigint NOT NULL,
    numero_matricula character varying(10) NOT NULL,
    data_matricula timestamp with time zone NOT NULL,
    data_atualizacao timestamp with time zone NOT NULL,
    observacoes text NOT NULL,
    inscricao_id bigint NOT NULL,
    interessado_id bigint NOT NULL,
    turma_id bigint NOT NULL,
    status_id bigint NOT NULL
);


ALTER TABLE public.academico_matricula OWNER TO metareciclagem_user;

--
-- Name: academico_matricula_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.academico_matricula ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.academico_matricula_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: academico_statusmatricula; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.academico_statusmatricula (
    id bigint NOT NULL,
    nome character varying(50) NOT NULL,
    cor character varying(7) NOT NULL,
    ordem integer NOT NULL,
    CONSTRAINT academico_statusmatricula_ordem_check CHECK ((ordem >= 0))
);


ALTER TABLE public.academico_statusmatricula OWNER TO metareciclagem_user;

--
-- Name: academico_statusmatricula_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.academico_statusmatricula ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.academico_statusmatricula_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: accounts_usuario; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.accounts_usuario (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    cpf character varying(11) NOT NULL,
    setor_trabalho character varying(50) NOT NULL,
    local_trabalho character varying(50) NOT NULL,
    telefone character varying(11) NOT NULL,
    celular character varying(11) NOT NULL,
    must_change_password boolean NOT NULL
);


ALTER TABLE public.accounts_usuario OWNER TO metareciclagem_user;

--
-- Name: accounts_usuario_groups; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.accounts_usuario_groups (
    id bigint NOT NULL,
    usuario_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.accounts_usuario_groups OWNER TO metareciclagem_user;

--
-- Name: accounts_usuario_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.accounts_usuario_groups ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.accounts_usuario_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: accounts_usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.accounts_usuario ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.accounts_usuario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: accounts_usuario_user_permissions; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.accounts_usuario_user_permissions (
    id bigint NOT NULL,
    usuario_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.accounts_usuario_user_permissions OWNER TO metareciclagem_user;

--
-- Name: accounts_usuario_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.accounts_usuario_user_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.accounts_usuario_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO metareciclagem_user;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.auth_group ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO metareciclagem_user;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.auth_group_permissions ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO metareciclagem_user;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.auth_permission ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: axes_accessattempt; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.axes_accessattempt (
    id integer NOT NULL,
    user_agent character varying(255) NOT NULL,
    ip_address inet,
    username character varying(255),
    http_accept character varying(1025) NOT NULL,
    path_info character varying(255) NOT NULL,
    attempt_time timestamp with time zone NOT NULL,
    get_data text NOT NULL,
    post_data text NOT NULL,
    failures_since_start integer NOT NULL,
    CONSTRAINT axes_accessattempt_failures_since_start_check CHECK ((failures_since_start >= 0))
);


ALTER TABLE public.axes_accessattempt OWNER TO metareciclagem_user;

--
-- Name: axes_accessattempt_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.axes_accessattempt ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.axes_accessattempt_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: axes_accessattemptexpiration; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.axes_accessattemptexpiration (
    access_attempt_id integer NOT NULL,
    expires_at timestamp with time zone NOT NULL
);


ALTER TABLE public.axes_accessattemptexpiration OWNER TO metareciclagem_user;

--
-- Name: axes_accessfailurelog; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.axes_accessfailurelog (
    id integer NOT NULL,
    user_agent character varying(255) NOT NULL,
    ip_address inet,
    username character varying(255),
    http_accept character varying(1025) NOT NULL,
    path_info character varying(255) NOT NULL,
    attempt_time timestamp with time zone NOT NULL,
    locked_out boolean NOT NULL
);


ALTER TABLE public.axes_accessfailurelog OWNER TO metareciclagem_user;

--
-- Name: axes_accessfailurelog_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.axes_accessfailurelog ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.axes_accessfailurelog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: axes_accesslog; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.axes_accesslog (
    id integer NOT NULL,
    user_agent character varying(255) NOT NULL,
    ip_address inet,
    username character varying(255),
    http_accept character varying(1025) NOT NULL,
    path_info character varying(255) NOT NULL,
    attempt_time timestamp with time zone NOT NULL,
    logout_time timestamp with time zone,
    session_hash character varying(64) NOT NULL
);


ALTER TABLE public.axes_accesslog OWNER TO metareciclagem_user;

--
-- Name: axes_accesslog_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.axes_accesslog ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.axes_accesslog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO metareciclagem_user;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.django_admin_log ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO metareciclagem_user;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.django_content_type ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO metareciclagem_user;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.django_migrations ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO metareciclagem_user;

--
-- Name: eventos_criterio; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.eventos_criterio (
    id bigint NOT NULL,
    tipo_criterio character varying(20) NOT NULL,
    codigo character varying(30) NOT NULL,
    nome character varying(200) NOT NULL,
    descricao text NOT NULL,
    pontos integer,
    categoria character varying(50) NOT NULL,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL
);


ALTER TABLE public.eventos_criterio OWNER TO metareciclagem_user;

--
-- Name: eventos_criterio_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.eventos_criterio ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.eventos_criterio_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: eventos_evento; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.eventos_evento (
    id bigint NOT NULL,
    nome character varying(200) NOT NULL,
    descricao text NOT NULL,
    total_vagas integer NOT NULL,
    data_inicio_inscricao timestamp with time zone NOT NULL,
    data_fim_inscricao timestamp with time zone NOT NULL,
    data_inicio_evento date NOT NULL,
    data_fim_evento date NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL,
    status_id bigint NOT NULL
);


ALTER TABLE public.eventos_evento OWNER TO metareciclagem_user;

--
-- Name: eventos_evento_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.eventos_evento ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.eventos_evento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: eventos_eventocriterio; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.eventos_eventocriterio (
    id bigint NOT NULL,
    prioridade integer NOT NULL,
    ativo boolean NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    criterio_id bigint NOT NULL,
    evento_id bigint NOT NULL
);


ALTER TABLE public.eventos_eventocriterio OWNER TO metareciclagem_user;

--
-- Name: eventos_eventocriterio_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.eventos_eventocriterio ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.eventos_eventocriterio_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: eventos_horario; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.eventos_horario (
    id bigint NOT NULL,
    dia_semana integer NOT NULL,
    hora_inicio time without time zone NOT NULL,
    hora_fim time without time zone NOT NULL,
    turma_id bigint NOT NULL
);


ALTER TABLE public.eventos_horario OWNER TO metareciclagem_user;

--
-- Name: eventos_horario_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.eventos_horario ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.eventos_horario_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: eventos_status; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.eventos_status (
    id bigint NOT NULL,
    nome character varying(50) NOT NULL,
    cor character varying(7) NOT NULL,
    ordem integer NOT NULL
);


ALTER TABLE public.eventos_status OWNER TO metareciclagem_user;

--
-- Name: eventos_status_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.eventos_status ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.eventos_status_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: eventos_turma; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.eventos_turma (
    id bigint NOT NULL,
    nome character varying(100) NOT NULL,
    turno character varying(20) NOT NULL,
    capacidade integer NOT NULL,
    local character varying(200) NOT NULL,
    data_inicio date NOT NULL,
    data_fim date NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL,
    evento_id bigint NOT NULL
);


ALTER TABLE public.eventos_turma OWNER TO metareciclagem_user;

--
-- Name: eventos_turma_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.eventos_turma ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.eventos_turma_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: interessados_fototipo; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.interessados_fototipo (
    id bigint NOT NULL,
    nome character varying(50) NOT NULL,
    descricao text NOT NULL
);


ALTER TABLE public.interessados_fototipo OWNER TO metareciclagem_user;

--
-- Name: interessados_fototipo_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.interessados_fototipo ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.interessados_fototipo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: interessados_interessado; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.interessados_interessado (
    id bigint NOT NULL,
    senha character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_superuser boolean NOT NULL,
    cpf text NOT NULL,
    nome character varying(50) NOT NULL,
    rg character varying(20) NOT NULL,
    data_nascimento date,
    cidade_nascimento character varying(50) NOT NULL,
    uf_nascimento character varying(2) NOT NULL,
    nacionalidade character varying(50) NOT NULL,
    endereco_residencial character varying(50) NOT NULL,
    num_endereco character varying(7) NOT NULL,
    bairro character varying(30) NOT NULL,
    complemento character varying(50) NOT NULL,
    cidade_residencia character varying(50) NOT NULL,
    uf_residencia character varying(2) NOT NULL,
    telefone character varying(11) NOT NULL,
    celular character varying(11) NOT NULL,
    email character varying(100),
    escolaridade character varying(30) NOT NULL,
    programa_social boolean NOT NULL,
    num_nis text NOT NULL,
    necessidades_especiais boolean NOT NULL,
    pcd_fisica boolean NOT NULL,
    pcd_visual boolean NOT NULL,
    pcd_auditiva boolean NOT NULL,
    pcd_intelectual boolean NOT NULL,
    pcd_psicossocial boolean NOT NULL,
    pcd_multiplas boolean NOT NULL,
    nome_responsavel character varying(50) NOT NULL,
    telefone_responsavel character varying(11) NOT NULL,
    celular_responsavel character varying(11) NOT NULL,
    email_responsavel character varying(100) NOT NULL,
    observacao text NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL,
    fototipo_id bigint,
    sexo_id bigint,
    cep character varying(8) NOT NULL,
    must_change_password boolean NOT NULL,
    cpf_hash character varying(64) NOT NULL,
    consentimento_lgpd boolean NOT NULL,
    consentimento_lgpd_em timestamp with time zone
);


ALTER TABLE public.interessados_interessado OWNER TO metareciclagem_user;

--
-- Name: interessados_interessado_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.interessados_interessado ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.interessados_interessado_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: interessados_passwordresettoken; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.interessados_passwordresettoken (
    id bigint NOT NULL,
    token character varying(100) NOT NULL,
    criado_em timestamp with time zone NOT NULL,
    expira_em timestamp with time zone NOT NULL,
    usado boolean NOT NULL,
    interessado_id bigint NOT NULL
);


ALTER TABLE public.interessados_passwordresettoken OWNER TO metareciclagem_user;

--
-- Name: interessados_passwordresettoken_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.interessados_passwordresettoken ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.interessados_passwordresettoken_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: interessados_sexo; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.interessados_sexo (
    id bigint NOT NULL,
    nome character varying(20) NOT NULL
);


ALTER TABLE public.interessados_sexo OWNER TO metareciclagem_user;

--
-- Name: interessados_sexo_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.interessados_sexo ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.interessados_sexo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: interessados_solicitacaoexclusao; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.interessados_solicitacaoexclusao (
    id bigint NOT NULL,
    nome_solicitante character varying(50) NOT NULL,
    email_solicitante character varying(254) NOT NULL,
    motivo text NOT NULL,
    status character varying(10) NOT NULL,
    solicitado_em timestamp with time zone NOT NULL,
    analisado_em timestamp with time zone,
    parecer_staff text NOT NULL,
    analisado_por_id bigint,
    interessado_id bigint
);


ALTER TABLE public.interessados_solicitacaoexclusao OWNER TO metareciclagem_user;

--
-- Name: interessados_solicitacaoexclusao_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.interessados_solicitacaoexclusao ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.interessados_solicitacaoexclusao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: selecao_classificacao; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.selecao_classificacao (
    id bigint NOT NULL,
    posicao integer,
    pontuacao_total numeric(10,2) NOT NULL,
    classificado boolean NOT NULL,
    lista_espera boolean NOT NULL,
    processado_em timestamp with time zone NOT NULL,
    atualizado_em timestamp with time zone NOT NULL,
    inscricao_id bigint NOT NULL,
    CONSTRAINT selecao_classificacao_posicao_check CHECK ((posicao >= 0))
);


ALTER TABLE public.selecao_classificacao OWNER TO metareciclagem_user;

--
-- Name: selecao_classificacao_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.selecao_classificacao ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.selecao_classificacao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: selecao_inscricao; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.selecao_inscricao (
    id bigint NOT NULL,
    data_inscricao timestamp with time zone NOT NULL,
    data_atualizacao timestamp with time zone NOT NULL,
    observacoes text NOT NULL,
    evento_id bigint NOT NULL,
    interessado_id bigint NOT NULL,
    status_id bigint NOT NULL
);


ALTER TABLE public.selecao_inscricao OWNER TO metareciclagem_user;

--
-- Name: selecao_inscricao_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.selecao_inscricao ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.selecao_inscricao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: selecao_inscricaocriterioatendido; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.selecao_inscricaocriterioatendido (
    id bigint NOT NULL,
    pontos_atribuidos integer NOT NULL,
    validado boolean NOT NULL,
    observacao_validacao text NOT NULL,
    criterio_id bigint NOT NULL,
    inscricao_id bigint NOT NULL,
    CONSTRAINT selecao_inscricaocriterioatendido_pontos_atribuidos_check CHECK ((pontos_atribuidos >= 0))
);


ALTER TABLE public.selecao_inscricaocriterioatendido OWNER TO metareciclagem_user;

--
-- Name: selecao_inscricaocriterioatendido_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.selecao_inscricaocriterioatendido ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.selecao_inscricaocriterioatendido_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: selecao_statusinscricao; Type: TABLE; Schema: public; Owner: metareciclagem_user
--

CREATE TABLE public.selecao_statusinscricao (
    id bigint NOT NULL,
    nome character varying(50) NOT NULL,
    cor character varying(7) NOT NULL,
    ordem integer NOT NULL,
    CONSTRAINT selecao_statusinscricao_ordem_check CHECK ((ordem >= 0))
);


ALTER TABLE public.selecao_statusinscricao OWNER TO metareciclagem_user;

--
-- Name: selecao_statusinscricao_id_seq; Type: SEQUENCE; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE public.selecao_statusinscricao ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.selecao_statusinscricao_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: academico_avaliacao; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.academico_avaliacao (id, nota_final, frequencia, aprovado, observacoes, certificado_emitido, data_emissao_certificado, avaliado_em, atualizado_em, matricula_id) FROM stdin;
\.


--
-- Data for Name: academico_matricula; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.academico_matricula (id, numero_matricula, data_matricula, data_atualizacao, observacoes, inscricao_id, interessado_id, turma_id, status_id) FROM stdin;
\.


--
-- Data for Name: academico_statusmatricula; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.academico_statusmatricula (id, nome, cor, ordem) FROM stdin;
\.


--
-- Data for Name: accounts_usuario; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.accounts_usuario (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, cpf, setor_trabalho, local_trabalho, telefone, celular, must_change_password) FROM stdin;
\.


--
-- Data for Name: accounts_usuario_groups; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.accounts_usuario_groups (id, usuario_id, group_id) FROM stdin;
\.


--
-- Data for Name: accounts_usuario_user_permissions; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.accounts_usuario_user_permissions (id, usuario_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add access attempt	6	add_accessattempt
22	Can change access attempt	6	change_accessattempt
23	Can delete access attempt	6	delete_accessattempt
24	Can view access attempt	6	view_accessattempt
25	Can add access log	7	add_accesslog
26	Can change access log	7	change_accesslog
27	Can delete access log	7	delete_accesslog
28	Can view access log	7	view_accesslog
29	Can add access failure	8	add_accessfailurelog
30	Can change access failure	8	change_accessfailurelog
31	Can delete access failure	8	delete_accessfailurelog
32	Can view access failure	8	view_accessfailurelog
33	Can add access attempt expiration	9	add_accessattemptexpiration
34	Can change access attempt expiration	9	change_accessattemptexpiration
35	Can delete access attempt expiration	9	delete_accessattemptexpiration
36	Can view access attempt expiration	9	view_accessattemptexpiration
37	Can add Usuário	10	add_usuario
38	Can change Usuário	10	change_usuario
39	Can delete Usuário	10	delete_usuario
40	Can view Usuário	10	view_usuario
41	Can add Fototipo	11	add_fototipo
42	Can change Fototipo	11	change_fototipo
43	Can delete Fototipo	11	delete_fototipo
44	Can view Fototipo	11	view_fototipo
45	Can add Sexo	12	add_sexo
46	Can change Sexo	12	change_sexo
47	Can delete Sexo	12	delete_sexo
48	Can view Sexo	12	view_sexo
49	Can add Interessado	13	add_interessado
50	Can change Interessado	13	change_interessado
51	Can delete Interessado	13	delete_interessado
52	Can view Interessado	13	view_interessado
53	Can add Token de Recuperação de Senha	14	add_passwordresettoken
54	Can change Token de Recuperação de Senha	14	change_passwordresettoken
55	Can delete Token de Recuperação de Senha	14	delete_passwordresettoken
56	Can view Token de Recuperação de Senha	14	view_passwordresettoken
57	Can add Solicitação de Exclusão	15	add_solicitacaoexclusao
58	Can change Solicitação de Exclusão	15	change_solicitacaoexclusao
59	Can delete Solicitação de Exclusão	15	delete_solicitacaoexclusao
60	Can view Solicitação de Exclusão	15	view_solicitacaoexclusao
61	Can add Critério de Classificação	16	add_criterio
62	Can change Critério de Classificação	16	change_criterio
63	Can delete Critério de Classificação	16	delete_criterio
64	Can view Critério de Classificação	16	view_criterio
65	Can add Status	17	add_status
66	Can change Status	17	change_status
67	Can delete Status	17	delete_status
68	Can view Status	17	view_status
69	Can add Evento	18	add_evento
70	Can change Evento	18	change_evento
71	Can delete Evento	18	delete_evento
72	Can view Evento	18	view_evento
73	Can add Turma	19	add_turma
74	Can change Turma	19	change_turma
75	Can delete Turma	19	delete_turma
76	Can view Turma	19	view_turma
77	Can add Horário	20	add_horario
78	Can change Horário	20	change_horario
79	Can delete Horário	20	delete_horario
80	Can view Horário	20	view_horario
81	Can add Critério do Evento	21	add_eventocriterio
82	Can change Critério do Evento	21	change_eventocriterio
83	Can delete Critério do Evento	21	delete_eventocriterio
84	Can view Critério do Evento	21	view_eventocriterio
85	Can add Status de Inscrição	22	add_statusinscricao
86	Can change Status de Inscrição	22	change_statusinscricao
87	Can delete Status de Inscrição	22	delete_statusinscricao
88	Can view Status de Inscrição	22	view_statusinscricao
89	Can add Inscrição	23	add_inscricao
90	Can change Inscrição	23	change_inscricao
91	Can delete Inscrição	23	delete_inscricao
92	Can view Inscrição	23	view_inscricao
93	Can add Classificação	24	add_classificacao
94	Can change Classificação	24	change_classificacao
95	Can delete Classificação	24	delete_classificacao
96	Can view Classificação	24	view_classificacao
97	Can add Critério Atendido	25	add_inscricaocriterioatendido
98	Can change Critério Atendido	25	change_inscricaocriterioatendido
99	Can delete Critério Atendido	25	delete_inscricaocriterioatendido
100	Can view Critério Atendido	25	view_inscricaocriterioatendido
101	Can add Status de Matrícula	26	add_statusmatricula
102	Can change Status de Matrícula	26	change_statusmatricula
103	Can delete Status de Matrícula	26	delete_statusmatricula
104	Can view Status de Matrícula	26	view_statusmatricula
105	Can add Matrícula	27	add_matricula
106	Can change Matrícula	27	change_matricula
107	Can delete Matrícula	27	delete_matricula
108	Can view Matrícula	27	view_matricula
109	Can add Avaliação	28	add_avaliacao
110	Can change Avaliação	28	change_avaliacao
111	Can delete Avaliação	28	delete_avaliacao
112	Can view Avaliação	28	view_avaliacao
\.


--
-- Data for Name: axes_accessattempt; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.axes_accessattempt (id, user_agent, ip_address, username, http_accept, path_info, attempt_time, get_data, post_data, failures_since_start) FROM stdin;
\.


--
-- Data for Name: axes_accessattemptexpiration; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.axes_accessattemptexpiration (access_attempt_id, expires_at) FROM stdin;
\.


--
-- Data for Name: axes_accessfailurelog; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.axes_accessfailurelog (id, user_agent, ip_address, username, http_accept, path_info, attempt_time, locked_out) FROM stdin;
\.


--
-- Data for Name: axes_accesslog; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.axes_accesslog (id, user_agent, ip_address, username, http_accept, path_info, attempt_time, logout_time, session_hash) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	axes	accessattempt
7	axes	accesslog
8	axes	accessfailurelog
9	axes	accessattemptexpiration
10	accounts	usuario
11	interessados	fototipo
12	interessados	sexo
13	interessados	interessado
14	interessados	passwordresettoken
15	interessados	solicitacaoexclusao
16	eventos	criterio
17	eventos	status
18	eventos	evento
19	eventos	turma
20	eventos	horario
21	eventos	eventocriterio
22	selecao	statusinscricao
23	selecao	inscricao
24	selecao	classificacao
25	selecao	inscricaocriterioatendido
26	academico	statusmatricula
27	academico	matricula
28	academico	avaliacao
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	interessados	0001_initial	2026-07-08 12:57:57.173195+00
2	eventos	0001_initial	2026-07-08 12:57:57.248534+00
3	selecao	0001_initial	2026-07-08 12:57:57.344497+00
4	interessados	0002_interessado_cep_interessado_raca_cor	2026-07-08 12:57:57.358919+00
5	interessados	0003_remove_interessado_raca_cor	2026-07-08 12:57:57.365478+00
6	interessados	0004_passwordresettoken	2026-07-08 12:57:57.387518+00
7	interessados	0005_interessado_must_change_password	2026-07-08 12:57:57.394482+00
8	academico	0001_initial	2026-07-08 12:57:57.496485+00
9	academico	0002_matricula_academico_m_inscric_af84a1_idx	2026-07-08 12:57:57.509051+00
10	contenttypes	0001_initial	2026-07-08 12:57:57.519272+00
11	contenttypes	0002_remove_content_type_name	2026-07-08 12:57:57.535561+00
12	auth	0001_initial	2026-07-08 12:57:57.575969+00
13	auth	0002_alter_permission_name_max_length	2026-07-08 12:57:57.580506+00
14	auth	0003_alter_user_email_max_length	2026-07-08 12:57:57.585161+00
15	auth	0004_alter_user_username_opts	2026-07-08 12:57:57.590234+00
16	auth	0005_alter_user_last_login_null	2026-07-08 12:57:57.595575+00
17	auth	0006_require_contenttypes_0002	2026-07-08 12:57:57.597402+00
18	auth	0007_alter_validators_add_error_messages	2026-07-08 12:57:57.602218+00
19	auth	0008_alter_user_username_max_length	2026-07-08 12:57:57.606812+00
20	auth	0009_alter_user_last_name_max_length	2026-07-08 12:57:57.611594+00
21	auth	0010_alter_group_name_max_length	2026-07-08 12:57:57.618209+00
22	auth	0011_update_proxy_permissions	2026-07-08 12:57:57.633032+00
23	auth	0012_alter_user_first_name_max_length	2026-07-08 12:57:57.637844+00
24	accounts	0001_initial	2026-07-08 12:57:57.686312+00
25	accounts	0002_usuario_must_change_password	2026-07-08 12:57:57.692981+00
26	accounts	0003_alter_usuario_email	2026-07-08 12:57:57.707762+00
27	admin	0001_initial	2026-07-08 12:57:57.730709+00
28	admin	0002_logentry_remove_auto_add	2026-07-08 12:57:57.736836+00
29	admin	0003_logentry_add_action_flag_choices	2026-07-08 12:57:57.743638+00
30	axes	0001_initial	2026-07-08 12:57:57.760321+00
31	axes	0002_auto_20151217_2044	2026-07-08 12:57:57.801053+00
32	axes	0003_auto_20160322_0929	2026-07-08 12:57:57.813137+00
33	axes	0004_auto_20181024_1538	2026-07-08 12:57:57.826858+00
34	axes	0005_remove_accessattempt_trusted	2026-07-08 12:57:57.830714+00
35	axes	0006_remove_accesslog_trusted	2026-07-08 12:57:57.834313+00
36	axes	0007_alter_accessattempt_unique_together	2026-07-08 12:57:57.857578+00
37	axes	0008_accessfailurelog	2026-07-08 12:57:57.879397+00
38	axes	0009_add_session_hash	2026-07-08 12:57:57.883197+00
39	axes	0010_accessattemptexpiration	2026-07-08 12:57:57.891514+00
40	interessados	0006_alter_interessado_email	2026-07-08 12:57:57.902317+00
41	interessados	0007_alter_interessado_cpf_alter_interessado_num_nis	2026-07-08 12:57:57.919393+00
42	interessados	0008_interessado_cpf_hash	2026-07-08 12:57:57.929469+00
43	interessados	0009_interessado_cpf_hash_unique	2026-07-08 12:57:57.942079+00
44	interessados	0010_interessado_consentimento_lgpd_and_more	2026-07-08 12:57:58.06941+00
45	interessados	0011_alter_interessado_consentimento_lgpd_and_more	2026-07-08 12:57:58.136134+00
46	interessados	0012_alter_interessado_cpf_alter_sexo_nome	2026-07-08 12:57:58.154919+00
47	selecao	0002_alter_classificacao_pontuacao_total_and_more	2026-07-08 12:57:58.168931+00
48	selecao	0003_alter_inscricao_data_inscricao	2026-07-08 12:57:58.18124+00
49	sessions	0001_initial	2026-07-08 12:57:58.195572+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: eventos_criterio; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.eventos_criterio (id, tipo_criterio, codigo, nome, descricao, pontos, categoria, ativo, criado_em, atualizado_em) FROM stdin;
\.


--
-- Data for Name: eventos_evento; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.eventos_evento (id, nome, descricao, total_vagas, data_inicio_inscricao, data_fim_inscricao, data_inicio_evento, data_fim_evento, criado_em, atualizado_em, status_id) FROM stdin;
\.


--
-- Data for Name: eventos_eventocriterio; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.eventos_eventocriterio (id, prioridade, ativo, criado_em, criterio_id, evento_id) FROM stdin;
\.


--
-- Data for Name: eventos_horario; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.eventos_horario (id, dia_semana, hora_inicio, hora_fim, turma_id) FROM stdin;
\.


--
-- Data for Name: eventos_status; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.eventos_status (id, nome, cor, ordem) FROM stdin;
\.


--
-- Data for Name: eventos_turma; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.eventos_turma (id, nome, turno, capacidade, local, data_inicio, data_fim, criado_em, atualizado_em, evento_id) FROM stdin;
\.


--
-- Data for Name: interessados_fototipo; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.interessados_fototipo (id, nome, descricao) FROM stdin;
\.


--
-- Data for Name: interessados_interessado; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.interessados_interessado (id, senha, last_login, is_active, is_staff, is_superuser, cpf, nome, rg, data_nascimento, cidade_nascimento, uf_nascimento, nacionalidade, endereco_residencial, num_endereco, bairro, complemento, cidade_residencia, uf_residencia, telefone, celular, email, escolaridade, programa_social, num_nis, necessidades_especiais, pcd_fisica, pcd_visual, pcd_auditiva, pcd_intelectual, pcd_psicossocial, pcd_multiplas, nome_responsavel, telefone_responsavel, celular_responsavel, email_responsavel, observacao, criado_em, atualizado_em, fototipo_id, sexo_id, cep, must_change_password, cpf_hash, consentimento_lgpd, consentimento_lgpd_em) FROM stdin;
\.


--
-- Data for Name: interessados_passwordresettoken; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.interessados_passwordresettoken (id, token, criado_em, expira_em, usado, interessado_id) FROM stdin;
\.


--
-- Data for Name: interessados_sexo; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.interessados_sexo (id, nome) FROM stdin;
\.


--
-- Data for Name: interessados_solicitacaoexclusao; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.interessados_solicitacaoexclusao (id, nome_solicitante, email_solicitante, motivo, status, solicitado_em, analisado_em, parecer_staff, analisado_por_id, interessado_id) FROM stdin;
\.


--
-- Data for Name: selecao_classificacao; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.selecao_classificacao (id, posicao, pontuacao_total, classificado, lista_espera, processado_em, atualizado_em, inscricao_id) FROM stdin;
\.


--
-- Data for Name: selecao_inscricao; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.selecao_inscricao (id, data_inscricao, data_atualizacao, observacoes, evento_id, interessado_id, status_id) FROM stdin;
\.


--
-- Data for Name: selecao_inscricaocriterioatendido; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.selecao_inscricaocriterioatendido (id, pontos_atribuidos, validado, observacao_validacao, criterio_id, inscricao_id) FROM stdin;
\.


--
-- Data for Name: selecao_statusinscricao; Type: TABLE DATA; Schema: public; Owner: metareciclagem_user
--

COPY public.selecao_statusinscricao (id, nome, cor, ordem) FROM stdin;
\.


--
-- Name: academico_avaliacao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.academico_avaliacao_id_seq', 1, false);


--
-- Name: academico_matricula_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.academico_matricula_id_seq', 1, false);


--
-- Name: academico_statusmatricula_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.academico_statusmatricula_id_seq', 1, false);


--
-- Name: accounts_usuario_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.accounts_usuario_groups_id_seq', 1, false);


--
-- Name: accounts_usuario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.accounts_usuario_id_seq', 1, false);


--
-- Name: accounts_usuario_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.accounts_usuario_user_permissions_id_seq', 1, false);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 112, true);


--
-- Name: axes_accessattempt_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.axes_accessattempt_id_seq', 1, false);


--
-- Name: axes_accessfailurelog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.axes_accessfailurelog_id_seq', 1, false);


--
-- Name: axes_accesslog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.axes_accesslog_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 28, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 49, true);


--
-- Name: eventos_criterio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.eventos_criterio_id_seq', 1, false);


--
-- Name: eventos_evento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.eventos_evento_id_seq', 1, false);


--
-- Name: eventos_eventocriterio_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.eventos_eventocriterio_id_seq', 1, false);


--
-- Name: eventos_horario_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.eventos_horario_id_seq', 1, false);


--
-- Name: eventos_status_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.eventos_status_id_seq', 1, false);


--
-- Name: eventos_turma_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.eventos_turma_id_seq', 1, false);


--
-- Name: interessados_fototipo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.interessados_fototipo_id_seq', 1, false);


--
-- Name: interessados_interessado_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.interessados_interessado_id_seq', 1, false);


--
-- Name: interessados_passwordresettoken_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.interessados_passwordresettoken_id_seq', 1, false);


--
-- Name: interessados_sexo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.interessados_sexo_id_seq', 1, false);


--
-- Name: interessados_solicitacaoexclusao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.interessados_solicitacaoexclusao_id_seq', 1, false);


--
-- Name: selecao_classificacao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.selecao_classificacao_id_seq', 1, false);


--
-- Name: selecao_inscricao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.selecao_inscricao_id_seq', 1, false);


--
-- Name: selecao_inscricaocriterioatendido_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.selecao_inscricaocriterioatendido_id_seq', 1, false);


--
-- Name: selecao_statusinscricao_id_seq; Type: SEQUENCE SET; Schema: public; Owner: metareciclagem_user
--

SELECT pg_catalog.setval('public.selecao_statusinscricao_id_seq', 1, false);


--
-- Name: academico_avaliacao academico_avaliacao_matricula_id_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_avaliacao
    ADD CONSTRAINT academico_avaliacao_matricula_id_key UNIQUE (matricula_id);


--
-- Name: academico_avaliacao academico_avaliacao_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_avaliacao
    ADD CONSTRAINT academico_avaliacao_pkey PRIMARY KEY (id);


--
-- Name: academico_matricula academico_matricula_numero_matricula_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_matricula
    ADD CONSTRAINT academico_matricula_numero_matricula_key UNIQUE (numero_matricula);


--
-- Name: academico_matricula academico_matricula_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_matricula
    ADD CONSTRAINT academico_matricula_pkey PRIMARY KEY (id);


--
-- Name: academico_matricula academico_matricula_turma_id_interessado_id_51257fc9_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_matricula
    ADD CONSTRAINT academico_matricula_turma_id_interessado_id_51257fc9_uniq UNIQUE (turma_id, interessado_id);


--
-- Name: academico_statusmatricula academico_statusmatricula_nome_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_statusmatricula
    ADD CONSTRAINT academico_statusmatricula_nome_key UNIQUE (nome);


--
-- Name: academico_statusmatricula academico_statusmatricula_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_statusmatricula
    ADD CONSTRAINT academico_statusmatricula_pkey PRIMARY KEY (id);


--
-- Name: accounts_usuario accounts_usuario_cpf_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario
    ADD CONSTRAINT accounts_usuario_cpf_key UNIQUE (cpf);


--
-- Name: accounts_usuario accounts_usuario_email_19c7414e_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario
    ADD CONSTRAINT accounts_usuario_email_19c7414e_uniq UNIQUE (email);


--
-- Name: accounts_usuario_groups accounts_usuario_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario_groups
    ADD CONSTRAINT accounts_usuario_groups_pkey PRIMARY KEY (id);


--
-- Name: accounts_usuario_groups accounts_usuario_groups_usuario_id_group_id_90f476d3_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario_groups
    ADD CONSTRAINT accounts_usuario_groups_usuario_id_group_id_90f476d3_uniq UNIQUE (usuario_id, group_id);


--
-- Name: accounts_usuario accounts_usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario
    ADD CONSTRAINT accounts_usuario_pkey PRIMARY KEY (id);


--
-- Name: accounts_usuario_user_permissions accounts_usuario_user_pe_usuario_id_permission_id_0065a2ce_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario_user_permissions
    ADD CONSTRAINT accounts_usuario_user_pe_usuario_id_permission_id_0065a2ce_uniq UNIQUE (usuario_id, permission_id);


--
-- Name: accounts_usuario_user_permissions accounts_usuario_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario_user_permissions
    ADD CONSTRAINT accounts_usuario_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: accounts_usuario accounts_usuario_username_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario
    ADD CONSTRAINT accounts_usuario_username_key UNIQUE (username);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: axes_accessattempt axes_accessattempt_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.axes_accessattempt
    ADD CONSTRAINT axes_accessattempt_pkey PRIMARY KEY (id);


--
-- Name: axes_accessattempt axes_accessattempt_username_ip_address_user_agent_8ea22282_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.axes_accessattempt
    ADD CONSTRAINT axes_accessattempt_username_ip_address_user_agent_8ea22282_uniq UNIQUE (username, ip_address, user_agent);


--
-- Name: axes_accessattemptexpiration axes_accessattemptexpiration_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.axes_accessattemptexpiration
    ADD CONSTRAINT axes_accessattemptexpiration_pkey PRIMARY KEY (access_attempt_id);


--
-- Name: axes_accessfailurelog axes_accessfailurelog_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.axes_accessfailurelog
    ADD CONSTRAINT axes_accessfailurelog_pkey PRIMARY KEY (id);


--
-- Name: axes_accesslog axes_accesslog_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.axes_accesslog
    ADD CONSTRAINT axes_accesslog_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: eventos_criterio eventos_criterio_codigo_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_criterio
    ADD CONSTRAINT eventos_criterio_codigo_key UNIQUE (codigo);


--
-- Name: eventos_criterio eventos_criterio_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_criterio
    ADD CONSTRAINT eventos_criterio_pkey PRIMARY KEY (id);


--
-- Name: eventos_evento eventos_evento_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_evento
    ADD CONSTRAINT eventos_evento_pkey PRIMARY KEY (id);


--
-- Name: eventos_eventocriterio eventos_eventocriterio_evento_id_criterio_id_9ee1bd55_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_eventocriterio
    ADD CONSTRAINT eventos_eventocriterio_evento_id_criterio_id_9ee1bd55_uniq UNIQUE (evento_id, criterio_id);


--
-- Name: eventos_eventocriterio eventos_eventocriterio_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_eventocriterio
    ADD CONSTRAINT eventos_eventocriterio_pkey PRIMARY KEY (id);


--
-- Name: eventos_horario eventos_horario_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_horario
    ADD CONSTRAINT eventos_horario_pkey PRIMARY KEY (id);


--
-- Name: eventos_status eventos_status_nome_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_status
    ADD CONSTRAINT eventos_status_nome_key UNIQUE (nome);


--
-- Name: eventos_status eventos_status_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_status
    ADD CONSTRAINT eventos_status_pkey PRIMARY KEY (id);


--
-- Name: eventos_turma eventos_turma_evento_id_nome_8d323f73_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_turma
    ADD CONSTRAINT eventos_turma_evento_id_nome_8d323f73_uniq UNIQUE (evento_id, nome);


--
-- Name: eventos_turma eventos_turma_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_turma
    ADD CONSTRAINT eventos_turma_pkey PRIMARY KEY (id);


--
-- Name: interessados_fototipo interessados_fototipo_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_fototipo
    ADD CONSTRAINT interessados_fototipo_pkey PRIMARY KEY (id);


--
-- Name: interessados_interessado interessados_interessado_cpf_hash_0c279a5c_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_interessado
    ADD CONSTRAINT interessados_interessado_cpf_hash_0c279a5c_uniq UNIQUE (cpf_hash);


--
-- Name: interessados_interessado interessados_interessado_cpf_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_interessado
    ADD CONSTRAINT interessados_interessado_cpf_key UNIQUE (cpf);


--
-- Name: interessados_interessado interessados_interessado_email_004f6a1a_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_interessado
    ADD CONSTRAINT interessados_interessado_email_004f6a1a_uniq UNIQUE (email);


--
-- Name: interessados_interessado interessados_interessado_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_interessado
    ADD CONSTRAINT interessados_interessado_pkey PRIMARY KEY (id);


--
-- Name: interessados_passwordresettoken interessados_passwordresettoken_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_passwordresettoken
    ADD CONSTRAINT interessados_passwordresettoken_pkey PRIMARY KEY (id);


--
-- Name: interessados_passwordresettoken interessados_passwordresettoken_token_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_passwordresettoken
    ADD CONSTRAINT interessados_passwordresettoken_token_key UNIQUE (token);


--
-- Name: interessados_sexo interessados_sexo_nome_c6c8ae4e_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_sexo
    ADD CONSTRAINT interessados_sexo_nome_c6c8ae4e_uniq UNIQUE (nome);


--
-- Name: interessados_sexo interessados_sexo_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_sexo
    ADD CONSTRAINT interessados_sexo_pkey PRIMARY KEY (id);


--
-- Name: interessados_solicitacaoexclusao interessados_solicitacaoexclusao_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_solicitacaoexclusao
    ADD CONSTRAINT interessados_solicitacaoexclusao_pkey PRIMARY KEY (id);


--
-- Name: selecao_classificacao selecao_classificacao_inscricao_id_32f20847_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_classificacao
    ADD CONSTRAINT selecao_classificacao_inscricao_id_32f20847_uniq UNIQUE (inscricao_id);


--
-- Name: selecao_classificacao selecao_classificacao_inscricao_id_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_classificacao
    ADD CONSTRAINT selecao_classificacao_inscricao_id_key UNIQUE (inscricao_id);


--
-- Name: selecao_classificacao selecao_classificacao_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_classificacao
    ADD CONSTRAINT selecao_classificacao_pkey PRIMARY KEY (id);


--
-- Name: selecao_inscricao selecao_inscricao_interessado_id_evento_id_a51d630a_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_inscricao
    ADD CONSTRAINT selecao_inscricao_interessado_id_evento_id_a51d630a_uniq UNIQUE (interessado_id, evento_id);


--
-- Name: selecao_inscricao selecao_inscricao_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_inscricao
    ADD CONSTRAINT selecao_inscricao_pkey PRIMARY KEY (id);


--
-- Name: selecao_inscricaocriterioatendido selecao_inscricaocriteri_inscricao_id_criterio_id_c88c00eb_uniq; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_inscricaocriterioatendido
    ADD CONSTRAINT selecao_inscricaocriteri_inscricao_id_criterio_id_c88c00eb_uniq UNIQUE (inscricao_id, criterio_id);


--
-- Name: selecao_inscricaocriterioatendido selecao_inscricaocriterioatendido_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_inscricaocriterioatendido
    ADD CONSTRAINT selecao_inscricaocriterioatendido_pkey PRIMARY KEY (id);


--
-- Name: selecao_statusinscricao selecao_statusinscricao_nome_key; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_statusinscricao
    ADD CONSTRAINT selecao_statusinscricao_nome_key UNIQUE (nome);


--
-- Name: selecao_statusinscricao selecao_statusinscricao_pkey; Type: CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_statusinscricao
    ADD CONSTRAINT selecao_statusinscricao_pkey PRIMARY KEY (id);


--
-- Name: academico_m_inscric_af84a1_idx; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX academico_m_inscric_af84a1_idx ON public.academico_matricula USING btree (inscricao_id);


--
-- Name: academico_m_numero__4bc01b_idx; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX academico_m_numero__4bc01b_idx ON public.academico_matricula USING btree (numero_matricula);


--
-- Name: academico_m_turma_i_1f9f0d_idx; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX academico_m_turma_i_1f9f0d_idx ON public.academico_matricula USING btree (turma_id, interessado_id);


--
-- Name: academico_matricula_inscricao_id_a95f8468; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX academico_matricula_inscricao_id_a95f8468 ON public.academico_matricula USING btree (inscricao_id);


--
-- Name: academico_matricula_interessado_id_27c13dae; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX academico_matricula_interessado_id_27c13dae ON public.academico_matricula USING btree (interessado_id);


--
-- Name: academico_matricula_numero_matricula_63207837_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX academico_matricula_numero_matricula_63207837_like ON public.academico_matricula USING btree (numero_matricula varchar_pattern_ops);


--
-- Name: academico_matricula_status_id_c0fa5b2c; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX academico_matricula_status_id_c0fa5b2c ON public.academico_matricula USING btree (status_id);


--
-- Name: academico_matricula_turma_id_ada4fc93; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX academico_matricula_turma_id_ada4fc93 ON public.academico_matricula USING btree (turma_id);


--
-- Name: academico_statusmatricula_nome_f1319f70_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX academico_statusmatricula_nome_f1319f70_like ON public.academico_statusmatricula USING btree (nome varchar_pattern_ops);


--
-- Name: accounts_usuario_cpf_88f87c69_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX accounts_usuario_cpf_88f87c69_like ON public.accounts_usuario USING btree (cpf varchar_pattern_ops);


--
-- Name: accounts_usuario_email_19c7414e_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX accounts_usuario_email_19c7414e_like ON public.accounts_usuario USING btree (email varchar_pattern_ops);


--
-- Name: accounts_usuario_groups_group_id_81d91a41; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX accounts_usuario_groups_group_id_81d91a41 ON public.accounts_usuario_groups USING btree (group_id);


--
-- Name: accounts_usuario_groups_usuario_id_8eb16911; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX accounts_usuario_groups_usuario_id_8eb16911 ON public.accounts_usuario_groups USING btree (usuario_id);


--
-- Name: accounts_usuario_user_permissions_permission_id_3de42c14; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX accounts_usuario_user_permissions_permission_id_3de42c14 ON public.accounts_usuario_user_permissions USING btree (permission_id);


--
-- Name: accounts_usuario_user_permissions_usuario_id_d048ad71; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX accounts_usuario_user_permissions_usuario_id_d048ad71 ON public.accounts_usuario_user_permissions USING btree (usuario_id);


--
-- Name: accounts_usuario_username_c366c69f_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX accounts_usuario_username_c366c69f_like ON public.accounts_usuario USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: axes_accessattempt_ip_address_10922d9c; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessattempt_ip_address_10922d9c ON public.axes_accessattempt USING btree (ip_address);


--
-- Name: axes_accessattempt_user_agent_ad89678b; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessattempt_user_agent_ad89678b ON public.axes_accessattempt USING btree (user_agent);


--
-- Name: axes_accessattempt_user_agent_ad89678b_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessattempt_user_agent_ad89678b_like ON public.axes_accessattempt USING btree (user_agent varchar_pattern_ops);


--
-- Name: axes_accessattempt_username_3f2d4ca0; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessattempt_username_3f2d4ca0 ON public.axes_accessattempt USING btree (username);


--
-- Name: axes_accessattempt_username_3f2d4ca0_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessattempt_username_3f2d4ca0_like ON public.axes_accessattempt USING btree (username varchar_pattern_ops);


--
-- Name: axes_accessfailurelog_ip_address_2e9f5a7f; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessfailurelog_ip_address_2e9f5a7f ON public.axes_accessfailurelog USING btree (ip_address);


--
-- Name: axes_accessfailurelog_user_agent_ea145dda; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessfailurelog_user_agent_ea145dda ON public.axes_accessfailurelog USING btree (user_agent);


--
-- Name: axes_accessfailurelog_user_agent_ea145dda_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessfailurelog_user_agent_ea145dda_like ON public.axes_accessfailurelog USING btree (user_agent varchar_pattern_ops);


--
-- Name: axes_accessfailurelog_username_a8b7e8a4; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessfailurelog_username_a8b7e8a4 ON public.axes_accessfailurelog USING btree (username);


--
-- Name: axes_accessfailurelog_username_a8b7e8a4_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accessfailurelog_username_a8b7e8a4_like ON public.axes_accessfailurelog USING btree (username varchar_pattern_ops);


--
-- Name: axes_accesslog_ip_address_86b417e5; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accesslog_ip_address_86b417e5 ON public.axes_accesslog USING btree (ip_address);


--
-- Name: axes_accesslog_user_agent_0e659004; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accesslog_user_agent_0e659004 ON public.axes_accesslog USING btree (user_agent);


--
-- Name: axes_accesslog_user_agent_0e659004_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accesslog_user_agent_0e659004_like ON public.axes_accesslog USING btree (user_agent varchar_pattern_ops);


--
-- Name: axes_accesslog_username_df93064b; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accesslog_username_df93064b ON public.axes_accesslog USING btree (username);


--
-- Name: axes_accesslog_username_df93064b_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX axes_accesslog_username_df93064b_like ON public.axes_accesslog USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: eventos_criterio_codigo_b06552c8_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX eventos_criterio_codigo_b06552c8_like ON public.eventos_criterio USING btree (codigo varchar_pattern_ops);


--
-- Name: eventos_evento_status_id_412ac246; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX eventos_evento_status_id_412ac246 ON public.eventos_evento USING btree (status_id);


--
-- Name: eventos_eventocriterio_criterio_id_7e3b9bd4; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX eventos_eventocriterio_criterio_id_7e3b9bd4 ON public.eventos_eventocriterio USING btree (criterio_id);


--
-- Name: eventos_eventocriterio_evento_id_5f07f643; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX eventos_eventocriterio_evento_id_5f07f643 ON public.eventos_eventocriterio USING btree (evento_id);


--
-- Name: eventos_horario_turma_id_29c0bdff; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX eventos_horario_turma_id_29c0bdff ON public.eventos_horario USING btree (turma_id);


--
-- Name: eventos_status_nome_7b0c99ed_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX eventos_status_nome_7b0c99ed_like ON public.eventos_status USING btree (nome varchar_pattern_ops);


--
-- Name: eventos_turma_evento_id_63fb57f5; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX eventos_turma_evento_id_63fb57f5 ON public.eventos_turma USING btree (evento_id);


--
-- Name: interessados_interessado_cpf_b91198ed_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_interessado_cpf_b91198ed_like ON public.interessados_interessado USING btree (cpf text_pattern_ops);


--
-- Name: interessados_interessado_cpf_hash_0c279a5c_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_interessado_cpf_hash_0c279a5c_like ON public.interessados_interessado USING btree (cpf_hash varchar_pattern_ops);


--
-- Name: interessados_interessado_email_004f6a1a_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_interessado_email_004f6a1a_like ON public.interessados_interessado USING btree (email varchar_pattern_ops);


--
-- Name: interessados_interessado_fototipo_id_1bd82591; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_interessado_fototipo_id_1bd82591 ON public.interessados_interessado USING btree (fototipo_id);


--
-- Name: interessados_interessado_sexo_id_d912f7e0; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_interessado_sexo_id_d912f7e0 ON public.interessados_interessado USING btree (sexo_id);


--
-- Name: interessados_passwordresettoken_interessado_id_6d208345; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_passwordresettoken_interessado_id_6d208345 ON public.interessados_passwordresettoken USING btree (interessado_id);


--
-- Name: interessados_passwordresettoken_token_c8a8033f_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_passwordresettoken_token_c8a8033f_like ON public.interessados_passwordresettoken USING btree (token varchar_pattern_ops);


--
-- Name: interessados_sexo_nome_c6c8ae4e_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_sexo_nome_c6c8ae4e_like ON public.interessados_sexo USING btree (nome varchar_pattern_ops);


--
-- Name: interessados_solicitacaoexclusao_analisado_por_id_a4448b09; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_solicitacaoexclusao_analisado_por_id_a4448b09 ON public.interessados_solicitacaoexclusao USING btree (analisado_por_id);


--
-- Name: interessados_solicitacaoexclusao_interessado_id_72cb2d83; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX interessados_solicitacaoexclusao_interessado_id_72cb2d83 ON public.interessados_solicitacaoexclusao USING btree (interessado_id);


--
-- Name: selecao_inscricao_evento_id_69022fc4; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX selecao_inscricao_evento_id_69022fc4 ON public.selecao_inscricao USING btree (evento_id);


--
-- Name: selecao_inscricao_interessado_id_c7990ace; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX selecao_inscricao_interessado_id_c7990ace ON public.selecao_inscricao USING btree (interessado_id);


--
-- Name: selecao_inscricao_status_id_1747a6a8; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX selecao_inscricao_status_id_1747a6a8 ON public.selecao_inscricao USING btree (status_id);


--
-- Name: selecao_inscricaocriterioatendido_criterio_id_92a1333d; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX selecao_inscricaocriterioatendido_criterio_id_92a1333d ON public.selecao_inscricaocriterioatendido USING btree (criterio_id);


--
-- Name: selecao_inscricaocriterioatendido_inscricao_id_f4596be5; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX selecao_inscricaocriterioatendido_inscricao_id_f4596be5 ON public.selecao_inscricaocriterioatendido USING btree (inscricao_id);


--
-- Name: selecao_statusinscricao_nome_7e620433_like; Type: INDEX; Schema: public; Owner: metareciclagem_user
--

CREATE INDEX selecao_statusinscricao_nome_7e620433_like ON public.selecao_statusinscricao USING btree (nome varchar_pattern_ops);


--
-- Name: academico_avaliacao academico_avaliacao_matricula_id_0125d759_fk_academico; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_avaliacao
    ADD CONSTRAINT academico_avaliacao_matricula_id_0125d759_fk_academico FOREIGN KEY (matricula_id) REFERENCES public.academico_matricula(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: academico_matricula academico_matricula_inscricao_id_a95f8468_fk_selecao_i; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_matricula
    ADD CONSTRAINT academico_matricula_inscricao_id_a95f8468_fk_selecao_i FOREIGN KEY (inscricao_id) REFERENCES public.selecao_inscricao(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: academico_matricula academico_matricula_interessado_id_27c13dae_fk_interessa; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_matricula
    ADD CONSTRAINT academico_matricula_interessado_id_27c13dae_fk_interessa FOREIGN KEY (interessado_id) REFERENCES public.interessados_interessado(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: academico_matricula academico_matricula_status_id_c0fa5b2c_fk_academico; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_matricula
    ADD CONSTRAINT academico_matricula_status_id_c0fa5b2c_fk_academico FOREIGN KEY (status_id) REFERENCES public.academico_statusmatricula(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: academico_matricula academico_matricula_turma_id_ada4fc93_fk_eventos_turma_id; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.academico_matricula
    ADD CONSTRAINT academico_matricula_turma_id_ada4fc93_fk_eventos_turma_id FOREIGN KEY (turma_id) REFERENCES public.eventos_turma(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_usuario_groups accounts_usuario_gro_usuario_id_8eb16911_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario_groups
    ADD CONSTRAINT accounts_usuario_gro_usuario_id_8eb16911_fk_accounts_ FOREIGN KEY (usuario_id) REFERENCES public.accounts_usuario(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_usuario_groups accounts_usuario_groups_group_id_81d91a41_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario_groups
    ADD CONSTRAINT accounts_usuario_groups_group_id_81d91a41_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_usuario_user_permissions accounts_usuario_use_permission_id_3de42c14_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario_user_permissions
    ADD CONSTRAINT accounts_usuario_use_permission_id_3de42c14_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: accounts_usuario_user_permissions accounts_usuario_use_usuario_id_d048ad71_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.accounts_usuario_user_permissions
    ADD CONSTRAINT accounts_usuario_use_usuario_id_d048ad71_fk_accounts_ FOREIGN KEY (usuario_id) REFERENCES public.accounts_usuario(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: axes_accessattemptexpiration axes_accessattemptex_access_attempt_id_6b73a47a_fk_axes_acce; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.axes_accessattemptexpiration
    ADD CONSTRAINT axes_accessattemptex_access_attempt_id_6b73a47a_fk_axes_acce FOREIGN KEY (access_attempt_id) REFERENCES public.axes_accessattempt(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_accounts_usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_accounts_usuario_id FOREIGN KEY (user_id) REFERENCES public.accounts_usuario(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eventos_evento eventos_evento_status_id_412ac246_fk_eventos_status_id; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_evento
    ADD CONSTRAINT eventos_evento_status_id_412ac246_fk_eventos_status_id FOREIGN KEY (status_id) REFERENCES public.eventos_status(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eventos_eventocriterio eventos_eventocriter_criterio_id_7e3b9bd4_fk_eventos_c; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_eventocriterio
    ADD CONSTRAINT eventos_eventocriter_criterio_id_7e3b9bd4_fk_eventos_c FOREIGN KEY (criterio_id) REFERENCES public.eventos_criterio(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eventos_eventocriterio eventos_eventocriterio_evento_id_5f07f643_fk_eventos_evento_id; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_eventocriterio
    ADD CONSTRAINT eventos_eventocriterio_evento_id_5f07f643_fk_eventos_evento_id FOREIGN KEY (evento_id) REFERENCES public.eventos_evento(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eventos_horario eventos_horario_turma_id_29c0bdff_fk_eventos_turma_id; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_horario
    ADD CONSTRAINT eventos_horario_turma_id_29c0bdff_fk_eventos_turma_id FOREIGN KEY (turma_id) REFERENCES public.eventos_turma(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: eventos_turma eventos_turma_evento_id_63fb57f5_fk_eventos_evento_id; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.eventos_turma
    ADD CONSTRAINT eventos_turma_evento_id_63fb57f5_fk_eventos_evento_id FOREIGN KEY (evento_id) REFERENCES public.eventos_evento(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: interessados_interessado interessados_interes_fototipo_id_1bd82591_fk_interessa; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_interessado
    ADD CONSTRAINT interessados_interes_fototipo_id_1bd82591_fk_interessa FOREIGN KEY (fototipo_id) REFERENCES public.interessados_fototipo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: interessados_interessado interessados_interes_sexo_id_d912f7e0_fk_interessa; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_interessado
    ADD CONSTRAINT interessados_interes_sexo_id_d912f7e0_fk_interessa FOREIGN KEY (sexo_id) REFERENCES public.interessados_sexo(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: interessados_passwordresettoken interessados_passwor_interessado_id_6d208345_fk_interessa; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_passwordresettoken
    ADD CONSTRAINT interessados_passwor_interessado_id_6d208345_fk_interessa FOREIGN KEY (interessado_id) REFERENCES public.interessados_interessado(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: interessados_solicitacaoexclusao interessados_solicit_analisado_por_id_a4448b09_fk_accounts_; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_solicitacaoexclusao
    ADD CONSTRAINT interessados_solicit_analisado_por_id_a4448b09_fk_accounts_ FOREIGN KEY (analisado_por_id) REFERENCES public.accounts_usuario(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: interessados_solicitacaoexclusao interessados_solicit_interessado_id_72cb2d83_fk_interessa; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.interessados_solicitacaoexclusao
    ADD CONSTRAINT interessados_solicit_interessado_id_72cb2d83_fk_interessa FOREIGN KEY (interessado_id) REFERENCES public.interessados_interessado(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: selecao_classificacao selecao_classificaca_inscricao_id_32f20847_fk_selecao_i; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_classificacao
    ADD CONSTRAINT selecao_classificaca_inscricao_id_32f20847_fk_selecao_i FOREIGN KEY (inscricao_id) REFERENCES public.selecao_inscricao(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: selecao_inscricao selecao_inscricao_evento_id_69022fc4_fk_eventos_evento_id; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_inscricao
    ADD CONSTRAINT selecao_inscricao_evento_id_69022fc4_fk_eventos_evento_id FOREIGN KEY (evento_id) REFERENCES public.eventos_evento(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: selecao_inscricao selecao_inscricao_interessado_id_c7990ace_fk_interessa; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_inscricao
    ADD CONSTRAINT selecao_inscricao_interessado_id_c7990ace_fk_interessa FOREIGN KEY (interessado_id) REFERENCES public.interessados_interessado(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: selecao_inscricao selecao_inscricao_status_id_1747a6a8_fk_selecao_s; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_inscricao
    ADD CONSTRAINT selecao_inscricao_status_id_1747a6a8_fk_selecao_s FOREIGN KEY (status_id) REFERENCES public.selecao_statusinscricao(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: selecao_inscricaocriterioatendido selecao_inscricaocri_criterio_id_92a1333d_fk_eventos_c; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_inscricaocriterioatendido
    ADD CONSTRAINT selecao_inscricaocri_criterio_id_92a1333d_fk_eventos_c FOREIGN KEY (criterio_id) REFERENCES public.eventos_criterio(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: selecao_inscricaocriterioatendido selecao_inscricaocri_inscricao_id_f4596be5_fk_selecao_i; Type: FK CONSTRAINT; Schema: public; Owner: metareciclagem_user
--

ALTER TABLE ONLY public.selecao_inscricaocriterioatendido
    ADD CONSTRAINT selecao_inscricaocri_inscricao_id_f4596be5_fk_selecao_i FOREIGN KEY (inscricao_id) REFERENCES public.selecao_inscricao(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

\unrestrict v9zDbaVjQrlgGcqirPD65WFwahpUrJTpsUzOtH643b8IPpB8FHZzWvw7HdygrLl

