pepperTvDashboard = {
    refreshAppsInfoEvery: 15, // Minutes
    init: function() {
        this.loadAppsInfo();

        window.setInterval(this.loadAppsInfo, this.refreshAppsInfoEvery * 60 * 1000);
    },
    loadAppsInfo: function() {
        $.ajax({
            type: 'GET',
            url: this.apps_info_endpoint,
            success: function(response, status, xhr) {
                $.each(response, function(site_id, stores) {
                    var site_div = $('.site.' + site_id);

                    $.each(stores, function(store_id, data) {
                        if (typeof data === 'string') {
                            // TODO Handle error message
                        } else {
                            if (data.rating) {
                                site_div.find('.rating .' + store_id).text(data.rating + '/5');
                            }

                            if (data.votes) {
                                site_div.find('.votes .' + store_id).text(data.votes);
                            }

                            if (data.detail) {
                                $.each(data.detail, function(stars_count, percentage) {
                                    site_div.find('.detail-' + stars_count + ' .' + store_id).text(percentage + '%');
                                });
                            }

                             if (data.version) {
                                site_div.find('.' + store_id + ' .version').text(data.version);
                            }
                       }
                    });
                });
            },
            error: function(xhr, errorType, error) {
                alert(error);
            }
        });
    }
};