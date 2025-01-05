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


class GlassdoorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "glassdoor"

    @property
    def original_file_name(self) -> "str":
        return "glassdoor.svg"

    @property
    def title(self) -> "str":
        return "Glassdoor"

    @property
    def primary_color(self) -> "str":
        return "#00A162"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Glassdoor</title>
     <path d="M14.1093.0006c-.0749-.0074-.1348.0522-.1348.127v3.451c0
 .0673.0537.1194.121.127 2.619.172 4.6092.9501 4.6092
 3.6814H13.086a.1343.1343 0 0 0-.1348.1347v8.9644c0
 .0748.06.1347.1348.1347h10.0034c.0748 0
 .1347-.0599.1347-.1347V7.342c0-2.2374-.7996-4.0558-2.4159-5.3279C19.3191.8469
 17.0874.1428 14.1093.0006ZM.9107 7.387a.1342.1342 0 0
 0-.1347.1347v8.9566c0 .0748.06.1347.1347.1347h5.6189c0 2.7313-1.9902
 3.5094-4.6091 3.6815-.0674.0075-.1192.0596-.1192.127v3.451c0
 .0747.06.1343.1348.1269 2.9781-.1422 5.2078-.8463 6.6969-2.0136
 1.6163-1.272 2.4159-3.0905 2.4159-5.3278V7.5217a.1343.1343 0 0
 0-.1348-.1347z" />
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
