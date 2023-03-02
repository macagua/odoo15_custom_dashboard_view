odoo.define('custom_dashboard_view.dashboard_action', function (require){
    "use strict";

    let AbstractAction = require('web.AbstractAction');
    let core = require('web.core');
    let QWeb = core.qweb;
    let rpc = require('web.rpc');
    let ajax = require('web.ajax');

    let CustomDashboard = AbstractAction.extend({
        template: 'CustomDashboard',

        init: function(parent, context) {
            this._super(parent, context);
            this.dashboards_templates = ['ProjectDashboard'];
            this.today_sale = [];
        },

        willStart: function() {
            let self = this;
            return $.when(ajax.loadLibs(this), this._super()).then(function() {
                return self.fetch_data();
            });
        },

        start: function() {
                let self = this;
                this.set("title", 'Dashboard');
                return this._super().then(function() {
                    self.render_dashboards();
                });
        },

        render_dashboards: function(){
            let self = this;
            _.each(this.dashboards_templates, function(template) {
                self.$('.o_project_dashboard').append(
                    QWeb.render(template, {widget: self})
                );
            });
        },

        fetch_data: function() {
            let self = this;
            let result_set =  this._rpc({
                model: 'project.project',
                method: 'get_tiles_data'
            }).then(function(result){
                self.total_projects = result['total_projects'],
                self.total_tasks = result['total_tasks'],
                self.total_employees = result['total_employees']
            });
            return $.when(result_set);
        },
    })

    core.action_registry.add('custom_dashboard_view_tags', CustomDashboard);
    return CustomDashboard;
})
