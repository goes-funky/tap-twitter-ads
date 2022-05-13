# streams.py
# streams: API URL endpoints to be called
# properties:
#   <root node>: Plural stream name for the endpoint
#   path: API endpoint relative path, when added to the base URL, creates the full path,
#       default = stream_name
#   key_properties: Primary key fields for identifying an endpoint record.
#   replication_method: INCREMENTAL or FULL_TABLE
#   replication_keys: bookmark_field(s), typically a date-time, used for filtering the results
#        and setting the state
#   params: Query, sort, and other endpoint specific parameters; default = {}
#   data_key: JSON element containing the results list for the endpoint
#   bookmark_query_field: From date-time field used for filtering the query
#   bookmark_type: Data type for bookmark, integer or datetime

# pylint: disable=line-too-long
STREAMS = {
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/accounts#accounts
    'accounts': {
        'path': 'accounts',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'account_ids': '{account_ids}',
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/twitter-ads-api/campaign-management/api-reference/account-apps
    'account_apps': {
        'path': 'accounts/{account_id}/account_apps',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'account_ids': '{account_ids}',
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/account-media#account-media
    'account_media': {
        'path': 'accounts/{account_id}/account_media',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/advertiser-business
    # -categories#advertiser-business-categories
    'advertiser_business_categories': {
        'path': 'advertiser_business_categories',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'FULL_TABLE',
        'params': {}
    },
    # [DEPRECATED] bidding_rules endpoint
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/bidding-rules#bidding-rules
    # 'bidding_rules': {
    #     'path': 'bidding_rules',
    #     'data_key': 'data',
    #     'key_properties': ['currency'],
    #     'replication_method': 'FULL_TABLE',
    #     'params': {}
    # },

    # Reference: https://developer.twitter.com/en/docs/twitter-ads-api/measurement/api-reference/app-event-tags
    'app_event_tags': {
        'path': 'accounts/{account_id}/app_event_tags',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/campaigns#campaigns
    'campaigns': {
        'path': 'accounts/{account_id}/campaigns',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/website#website-cards
    'cards_website': {
        'path': 'accounts/{account_id}/cards',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-website#video-website-cards
    'cards_video_website': {
        'path': 'accounts/{account_id}/cards/video_website',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/image-app-download#image-app
    # -download-cards
    'cards_image_app_download': {
        'path': 'accounts/{account_id}/cards/image_app_download',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-app-download#video-app
    # -download-cards
    'cards_video_app_download': {
        'path': 'accounts/{account_id}/cards/video_app_download',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/poll#poll-cards
    'cards_poll': {
        'path': 'accounts/{account_id}/cards/poll',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/image-conversation#image
    # -conversation-cards
    'cards_image_conversation': {
        'path': 'accounts/{account_id}/cards/image_conversation',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-conversation#video
    # -conversation-cards
    'cards_video_conversation': {
        'path': 'accounts/{account_id}/cards/video_conversation',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/image-direct-message#image-direct
    # -message-cards
    'cards_image_direct_message': {
        'path': 'accounts/{account_id}/cards/image_direct_message',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/video-direct-message#video-direct
    # -message-cards
    'cards_video_direct_message': {
        'path': 'accounts/{account_id}/cards/video_direct_message',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/content-categories
    # #content-categories
    'content_categories': {
        'path': 'content_categories',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'FULL_TABLE',
        'params': {
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/funding-instruments
    # #funding-instruments
    'funding_instruments': {
        'path': 'accounts/{account_id}/funding_instruments',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/iab-categories#iab
    # -categories
    'iab_categories': {
        'path': 'iab_categories',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'FULL_TABLE',
        'params': {}
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/line-items#line-items
    'line_items': {
        'path': 'accounts/{account_id}/line_items',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        },
        'children': {
            # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-criteria#targeting-criteria
            'targeting_criteria': {
                'path': 'accounts/{account_id}/targeting_criteria',
                'data_key': 'data',
                'key_properties': ['line_item_id', 'id', 'targeting_type', 'targeting_value'],
                'replication_method': 'FULL_TABLE',
                'parent_ids_limit': 200,
                'params': {
                    'line_item_ids': '{parent_ids}',  # up to 200 comma delim ids
                    'with_deleted': '{with_deleted}',
                    'count': 1000,
                    'cursor': None
                },
                'children': {
                    # Reference: https://developer.twitter.com/en/docs/twitter-ads-api/campaign-management/api-reference/audience-summary
                    'audience_estimate': {
                        'path': 'accounts/{account_id}/audience_estimate',  # ->  Forbidden - INSUFFICIENT_CLIENT_APPLICATION_PERMISSION
                        # 'path': 'accounts/{account_id}/audience_summary',
                        'data_key': 'data',
                        'key_properties': ['audience_size'],
                        'replication_method': 'INCREMENTAL',
                        'replication_keys': ['updated_at'],
                        'parent_ids_limit': 10,
                        'params': {
                            # fetch as param targeting criteria
                            'targeting_criteria': '{targeting_criteria}',
                            'sort_by': ['updated_at-desc'],
                            'with_deleted': '{with_deleted}',
                            'count': 1000,
                            'cursor': None,
                            'method': 'post'
                        }
                    }
                }
            }
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/media-creatives#media-creatives
    'media_creatives': {
        'path': 'accounts/{account_id}/media_creatives',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/preroll-call-to-actions#preroll
    # -call-to-actions
    'preroll_call_to_actions': {
        'path': 'accounts/{account_id}/preroll_call_to_actions',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # References: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-accounts
    # #promoted-accounts
    'promoted_accounts': {
        'path': 'accounts/{account_id}/promoted_accounts',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promoted-tweets#promoted
    # -tweets
    'promoted_tweets': {
        'path': 'accounts/{account_id}/promoted_tweets',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/promotable-users
    # #promotable-users
    'promotable_users': {
        'path': 'accounts/{account_id}/promotable_users',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/scheduled-promoted
    # -tweets#scheduled-promoted-tweets
    'scheduled_promoted_tweets': {
        'path': 'accounts/{account_id}/scheduled_promoted_tweets',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/twitter-ads-api/creatives/api-reference/scheduled-tweets
    'scheduled_tweets': {
        'path': 'accounts/{account_id}/scheduled_tweets',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 200,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/audiences/api-reference/tailored-audiences#tailored-audiences
    'tailored_audiences': {
        'path': 'accounts/{account_id}/custom_audiences',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['updated_at'],
        'params': {
            'sort_by': ['updated_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-app-store-categories
    'targeting_app_store_categories': {
        'path': 'targeting_criteria/app_store_categories',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'params': {}
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-conversations
    'targeting_conversations': {
        'path': 'targeting_criteria/conversations',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'params': {
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-devices
    'targeting_devices': {
        'path': 'targeting_criteria/devices',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'params': {
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-events
    'targeting_events': {
        'path': 'targeting_criteria/events',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'params': {
            'start_time': '{start_date}',
            'event_types': 'CONFERENCE,HOLIDAY,MUSIC_AND_ENTERTAINMENT,OTHER,POLITICS,RECURRING,SPORTS',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-interests
    'targeting_interests': {
        'path': 'targeting_criteria/interests',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'params': {
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-languages
    'targeting_languages': {
        'path': 'targeting_criteria/languages',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'params': {
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-locations
    'targeting_locations': {
        'path': 'targeting_criteria/locations',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'sub_types': ['{country_code_list}'],
        'params': {
            'country_code': '{sub_type}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-network-operators
    'targeting_network_operators': {
        'path': 'targeting_criteria/network_operators',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'sub_types': ['{country_code_list}'],
        'params': {
            'country_code': '{sub_type}',
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-platform-versions
    'targeting_platform_versions': {
        'path': 'targeting_criteria/platform_versions',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'params': {}
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-platforms
    'targeting_platforms': {
        'path': 'targeting_criteria/platforms',
        'data_key': 'data',
        'key_properties': ['targeting_value'],
        'replication_method': 'FULL_TABLE',
        'params': {
            'count': 1000,
            'cursor': None
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get
    # -targeting-criteria-tv-markets
    'targeting_tv_markets': {
        'path': 'targeting_criteria/tv_markets',
        'data_key': 'data',
        'key_properties': ['locale'],
        'replication_method': 'FULL_TABLE',
        'params': {},
        'children': {
            # Reference: https://developer.twitter.com/en/docs/ads/campaign-management/api-reference/targeting-options#get-targeting-criteria-tv-shows
            'targeting_tv_shows': {
                'path': 'targeting_criteria/tv_shows',
                'data_key': 'data',
                'key_properties': ['targeting_value'],
                'replication_method': 'FULL_TABLE',
                'parent_ids_limit': 1,
                'params': {
                    'locale': '{parent_ids}',
                    'count': 1000,
                    'cursor': None
                }
            }
        }
    },
    # Reference: https://developer.twitter.com/en/docs/ads/creatives/api-reference/tweets#get-accounts-account-id-scoped-timeline
    # Data Dictionary: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object
    # User Data Dictionary: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/user-object
    'tweets': {
        'path': 'accounts/{account_id}/tweets',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'INCREMENTAL',
        'replication_keys': ['created_at'],
        'datetime_format': '%a %b %d %H:%M:%S %z %Y',
        'sub_types': ['PUBLISHED', 'SCHEDULED'],  # NOT DRAFT
        'params': {
            'tweet_type': '{sub_type}',
            'timeline_type': 'ALL',
            'sort_by': ['created_at-desc'],
            'with_deleted': '{with_deleted}',
            'count': 1000,
            'cursor': None  # NOT include_mentions_and_replies
        }
    },
    # Reference: https://developer.twitter.com/en/docs/twitter-ads-api/campaign-management/api-reference/tracking-tags
    'tracking_tags': {
            'path': 'accounts/{account_id}/tracking_tags',
            'data_key': 'data',
            'key_properties': ['id'],
            'replication_method': 'INCREMENTAL',
            'replication_keys': ['updated_at'],
            'datetime_format': '%a %b %d %H:%M:%S %z %Y',
            'params': {
                'account_id': '{account_id}',
                'sort_by': ['updated_at-desc'],
                'with_deleted': '{with_deleted}',
                'count': 1000,
                'cursor': None  # NOT include_mentions_and_replies
            }
        },
    # Reference: https://developer.twitter.com/en/docs/twitter-ads-api/measurement/api-reference/web-event-tags
    'web_event_tags': {
        'path': 'accounts/{account_id}/web_event_tags',
        'data_key': 'data',
        'key_properties': ['id'],
        'replication_method': 'FULL_TABLE',
        'params': {}
    },

}
# pylint: enable=line-too-long

REPORTS = {
    # Reference: https://developer.twitter.com/en/docs/twitter-ads-api/analytics/api-reference/asynchronous

    # SEGMENTS
    # ['AGE', 'AMPLIFY_MARKETPLACE_PREROLL_VIDEOS', 'AMPLIFY_PUBLISHER_TWEETS', 'APP_STORE_CATEGORY',
    # 'AUDIENCES', 'CONVERSATIONS', 'CONVERSION_TAGS', 'DEVICES', 'EVENTS', 'GENDER', 'INTERESTS',
    # 'KEYWORDS', 'LANGUAGES', 'LOCATIONS', 'METROS', 'PLATFORM_VERSIONS', 'PLATFORMS', 'POSTAL_CODES',
    # 'REGIONS', 'SIMILAR_TO_FOLLOWERS_OF_USER', 'SWIPEABLE_MEDIA', 'TV_ADS', 'TV_SHOWS']
    "reports": [
        # ACCOUNT INSIGHTS - not segmented
        {
          "name": "account_insights",
          "entity": "ACCOUNT",
          "segment": "NO_SEGMENT",
          "granularity": "DAY"
        },
        # CAMPAIGN INSIGHTS - not segmented
        {
          "name": "campaign_insights",
          "entity": "CAMPAIGN",
          "segment": "NO_SEGMENT",
          "granularity": "DAY"
        },
        # CAMPAIGN INSIGHTS - not segmented
        {
          "name": "funding_instrument_insights",
          "entity": "FUNDING_INSTRUMENT",
          "segment": "NO_SEGMENT",
          "granularity": "DAY"
        },
        # LINE ITEM INSIGHTS - not segmented
        {
          "name": "line_item_insights",
          "entity": "LINE_ITEM",
          "segment": "NO_SEGMENT",
          "granularity": "DAY"
        },
        # MEDIA CREATIVE INSIGHTS - not segmented
        {
          "name": "media_creative_insights",
          "entity": "MEDIA_CREATIVE",
          "segment": "NO_SEGMENT",
          "granularity": "DAY"
        },
        # ORGANIC TWEET INSIGHTS - not segmented
        {
          "name": "organic_tweet_insights",
          "entity": "ORGANIC_TWEET",
          "segment": "NO_SEGMENT",
          "granularity": "DAY"
        },
        # PROMOTED TWEET INSIGHTS - not segmented
        {
          "name": "promoted_tweet_insights",
          "entity": "PROMOTED_TWEET",
          "segment": "NO_SEGMENT",
          "granularity": "DAY"
        },
        # PROMOTED ACCOUNT INSIGHTS - not segmented
        {
          "name": "promoted_account_insights",
          "entity": "PROMOTED_ACCOUNT",
          "segment": "NO_SEGMENT",
          "granularity": "DAY"
        }
      ]
}


# De-nest children nodes for Discovery mode
def flatten_streams():
    flat_streams = {}
    # Loop through parents
    for stream_name, endpoint_config in STREAMS.items():
        flat_streams[stream_name] = endpoint_config
        # Loop through children
        children = endpoint_config.get('children')
        if children:
            for child_stream_name, child_endpoint_config in children.items():
                flat_streams[child_stream_name] = child_endpoint_config
                flat_streams[child_stream_name]['parent_stream'] = stream_name
                grandchildren = child_endpoint_config.get('children')
                if grandchildren:
                    for grandchild_stream_name, grandchild_endpoint_config in grandchildren.items():
                        flat_streams[grandchild_stream_name] = grandchild_endpoint_config
                        flat_streams[grandchild_stream_name]['parent_stream'] = child_stream_name
                        flat_streams[grandchild_stream_name]['grandparent_stream'] = stream_name
    return flat_streams
