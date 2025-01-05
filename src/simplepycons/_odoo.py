#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class OdooIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "odoo"

    @property
    def original_file_name(self) -> "str":
        return "odoo.svg"

    @property
    def title(self) -> "str":
        return "Odoo"

    @property
    def primary_color(self) -> "str":
        return "#714B67"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Odoo</title>
     <path d="M21.1002 15.7957c-1.6015
 0-2.8997-1.2983-2.8997-2.8998s1.2983-2.8997 2.8997-2.8997c1.6015 0
 2.8998 1.2982 2.8998 2.8997 0 1.5999-1.2979 2.8998-2.8998
 2.8998zm0-1.2c.9388.0006 1.7003-.7601
 1.7008-1.6989.0004-.9388-.7602-1.7003-1.699-1.7007h-.0018c-.9388.0004-1.6994.7619-1.699
 1.7007.0005.9381.761 1.6985 1.699 1.699zm-6.0655 1.2c-1.6014
 0-2.8997-1.2983-2.8997-2.8998s1.2983-2.8997 2.8997-2.8997c1.6015 0
 2.8998 1.2982 2.8998 2.8997 0 1.5999-1.2999 2.8998-2.8998
 2.8998zm0-1.2c.9389.0006 1.7003-.7601
 1.7008-1.6989.0005-.9388-.7602-1.7003-1.699-1.7007h-.0018c-.9388.0004-1.6994.7619-1.699
 1.7007.0005.9381.761 1.6985 1.699 1.699zM11.865 12.858c0
 1.6199-1.2979 2.9378-2.8977 2.9378s-2.8998-1.314-2.8998-2.9358
 1.1799-2.8597 2.8998-2.8597c.6359 0 1.2239.134 1.6998.484v-1.68a.6.6
 0 0 1 1.2 0v4.0537h-.002zm-2.8977 1.7399c.9388.0005 1.7002-.7602
 1.7007-1.699.0005-.9388-.7602-1.7003-1.699-1.7007h-.0017c-.9389.0004-1.6995.7619-1.699
 1.7007.0004.9381.7608 1.6985 1.699 1.699zm-6.0675 1.1979C1.2983
 15.7957 0 14.4974 0 12.8959s1.2983-2.8997 2.8998-2.8997 2.8997 1.2982
 2.8997 2.8997c0 1.5999-1.2999 2.8998-2.8997 2.8998zm0-1.2c.9388.0006
 1.7002-.7601
 1.7007-1.699.0005-.9387-.7602-1.7002-1.699-1.7006h-.0017c-.9388.0004-1.6995.7619-1.699
 1.7007.0004.9381.7608 1.6985 1.699 1.699z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
