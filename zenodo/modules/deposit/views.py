# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2016 CERN.
#
# Zenodo is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Redirects for legacy URLs."""

from __future__ import absolute_import, print_function

from flask import Blueprint, redirect, request, url_for
from invenio_communities.models import Community

blueprint = Blueprint(
    'zenodo_deposit',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static',
)


@blueprint.route('/upload/')
@blueprint.route('/deposit/')
def legacy_index():
    """Legacy deposit."""
    c_id = request.args.get('c', type=str)
    if c_id:
        c = Community.get(c_id)
        return redirect('/communities/{0}/upload'.format(c.id))
    return redirect(url_for('invenio_deposit_ui.new'))


# @blueprint.route('/deposit/<int:deposit_id>/')
# def deposit_index():
#     """Legacy deposit."""
#     return redirect(url_for('invenio_deposit_ui.new', deposit_id=deposit_id))