-- SQL to consolidate posts table while preserving relationships

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS public.posts (
    date date PRIMARY KEY,
    -- Non-video posts from all platforms
    post_id_linkedin_no_video text,
    posted_at_linkedin_no_video date,
    num_likes_linkedin_no_video integer,
    num_comments_linkedin_no_video integer,
    num_reshares_linkedin_no_video integer,
    
    post_id_instagram_no_video text,
    posted_at_instagram_no_video date,
    num_likes_instagram_no_video integer,
    num_comments_instagram_no_video integer,
    
    post_id_twitter_no_video text,
    posted_at_twitter_no_video date,
    num_likes_twitter_no_video integer,
    num_comments_twitter_no_video integer,
    num_reshares_twitter_no_video integer,
    
    post_id_substack_no_video text,
    posted_at_substack_no_video date,
    num_likes_substack_no_video integer,
    num_comments_substack_no_video integer,
    num_reshares_substack_no_video integer,
    
    post_id_threads_no_video text,
    posted_at_threads_no_video date,
    num_likes_threads_no_video integer,
    num_comments_threads_no_video integer,
    num_reshares_threads_no_video integer,
    
    -- Video posts from all platforms
    post_id_linkedin_video text,
    posted_at_linkedin_video date,
    num_likes_linkedin_video integer,
    num_comments_linkedin_video integer,
    num_reshares_linkedin_video integer,
    
    post_id_instagram_video text,
    posted_at_instagram_video date,
    num_likes_instagram_video integer,
    num_comments_instagram_video integer,
    
    post_id_twitter_video text,
    posted_at_twitter_video date,
    num_likes_twitter_video integer,
    num_comments_twitter_video integer,
    num_reshares_twitter_video integer,
    
    post_id_substack_video text,
    posted_at_substack_video date,
    num_likes_substack_video integer,
    num_comments_substack_video integer,
    num_reshares_substack_video integer,
    
    post_id_threads_video text,
    posted_at_threads_video date,
    num_likes_threads_video integer,
    num_comments_threads_video integer,
    num_reshares_threads_video integer
);

-- Clear existing data while preserving table structure and relationships
TRUNCATE TABLE public.posts;

-- Insert new data
INSERT INTO public.posts
WITH
        linkedin_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments,
                num_reshares
            FROM public.linkedin_posts
            WHERE is_video = 1
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),

        linkedin_non_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments,
                num_reshares
            FROM public.linkedin_posts
            WHERE is_video = 0
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),

        instagram_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                'https://www.instagram.com/p/' || post_id as post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments
            FROM public.instagram_posts
            WHERE is_video = 1
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),

        instagram_non_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                'https://www.instagram.com/p/' || post_id as post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments
            FROM public.instagram_posts
            WHERE is_video = 0
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),

        twitter_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                'https://x.com/FerraroRoberto/status/' || post_id as post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments,
                num_reshares
            FROM public.twitter_posts
            WHERE is_video = 1
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),

        twitter_non_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                'https://x.com/FerraroRoberto/status/' || post_id as post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments,
                num_reshares
            FROM public.twitter_posts
            WHERE is_video = 0
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),

        substack_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                'https://substack.com/profile/11567179-roberto-ferraro/note/' || post_id as post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments,
                num_reshares
            FROM public.substack_posts
            WHERE is_video = 1
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),

        substack_non_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                'https://substack.com/profile/11567179-roberto-ferraro/note/' || post_id as post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments,
                num_reshares
            FROM public.substack_posts
            WHERE is_video = 0
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),

        threads_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                'https://www.threads.com/@ferraroroberto/post/' || post_id as post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments,
                num_reshares
            FROM public.threads_posts
            WHERE is_video = 1
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),

        threads_non_video AS (
            SELECT DISTINCT ON (date)
                date::date as date,
                'https://www.threads.com/@ferraroroberto/post/' || post_id as post_id,
                posted_at::date as posted_at,
                num_likes,
                num_comments,
                num_reshares
            FROM public.threads_posts
            WHERE is_video = 0
            AND posted_at::date = date::date - interval '1 day'
            ORDER BY date, posted_at ASC
        ),
        
        -- Create a unified dates table to use as the base for joins
        all_dates AS (
            SELECT date FROM linkedin_video
            UNION SELECT date FROM linkedin_non_video
            UNION SELECT date FROM instagram_video
            UNION SELECT date FROM instagram_non_video
            UNION SELECT date FROM twitter_video
            UNION SELECT date FROM twitter_non_video
            UNION SELECT date FROM substack_video
            UNION SELECT date FROM substack_non_video
            UNION SELECT date FROM threads_video
            UNION SELECT date FROM threads_non_video
        )

SELECT
    -- Date field
    d.date,
    
    -- Non-video posts from all platforms
    lnv.post_id as post_id_linkedin_no_video,
    lnv.posted_at as posted_at_linkedin_no_video,
    lnv.num_likes as num_likes_linkedin_no_video,
    lnv.num_comments as num_comments_linkedin_no_video,
    lnv.num_reshares as num_reshares_linkedin_no_video,
    
    inv.post_id as post_id_instagram_no_video,
    inv.posted_at as posted_at_instagram_no_video,
    inv.num_likes as num_likes_instagram_no_video,
    inv.num_comments as num_comments_instagram_no_video,
    
    tnv.post_id as post_id_twitter_no_video,
    tnv.posted_at as posted_at_twitter_no_video,
    tnv.num_likes as num_likes_twitter_no_video,
    tnv.num_comments as num_comments_twitter_no_video,
    tnv.num_reshares as num_reshares_twitter_no_video,
    
    snv.post_id as post_id_substack_no_video,
    snv.posted_at as posted_at_substack_no_video,
    snv.num_likes as num_likes_substack_no_video,
    snv.num_comments as num_comments_substack_no_video,
    snv.num_reshares as num_reshares_substack_no_video,
    
    thnv.post_id as post_id_threads_no_video,
    thnv.posted_at as posted_at_threads_no_video,
    thnv.num_likes as num_likes_threads_no_video,
    thnv.num_comments as num_comments_threads_no_video,
    thnv.num_reshares as num_reshares_threads_no_video,

    -- Video posts from all platforms
    lv.post_id as post_id_linkedin_video,
    lv.posted_at as posted_at_linkedin_video,
    lv.num_likes as num_likes_linkedin_video,
    lv.num_comments as num_comments_linkedin_video,
    lv.num_reshares as num_reshares_linkedin_video,
    
    iv.post_id as post_id_instagram_video,
    iv.posted_at as posted_at_instagram_video,
    iv.num_likes as num_likes_instagram_video,
    iv.num_comments as num_comments_instagram_video,
    
    tv.post_id as post_id_twitter_video,
    tv.posted_at as posted_at_twitter_video,
    tv.num_likes as num_likes_twitter_video,
    tv.num_comments as num_comments_twitter_video,
    tv.num_reshares as num_reshares_twitter_video,
    
    sv.post_id as post_id_substack_video,
    sv.posted_at as posted_at_substack_video,
    sv.num_likes as num_likes_substack_video,
    sv.num_comments as num_comments_substack_video,
    sv.num_reshares as num_reshares_substack_video,
    
    thv.post_id as post_id_threads_video,
    thv.posted_at as posted_at_threads_video,
    thv.num_likes as num_likes_threads_video,
    thv.num_comments as num_comments_threads_video,
    thv.num_reshares as num_reshares_threads_video
FROM all_dates d
    LEFT JOIN linkedin_video lv ON d.date = lv.date
    LEFT JOIN linkedin_non_video lnv ON d.date = lnv.date
    LEFT JOIN instagram_video iv ON d.date = iv.date
    LEFT JOIN instagram_non_video inv ON d.date = inv.date
    LEFT JOIN twitter_video tv ON d.date = tv.date
    LEFT JOIN twitter_non_video tnv ON d.date = tnv.date
    LEFT JOIN substack_video sv ON d.date = sv.date
    LEFT JOIN substack_non_video snv ON d.date = snv.date
    LEFT JOIN threads_video thv ON d.date = thv.date
    LEFT JOIN threads_non_video thnv ON d.date = thnv.date;

-- Add table comment if it doesn't exist
COMMENT ON TABLE public.posts IS 'Consolidated posts data from all platforms, separated by video/non-video, with one record per day';