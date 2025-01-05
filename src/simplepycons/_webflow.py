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


class WebflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webflow"

    @property
    def original_file_name(self) -> "str":
        return "webflow.svg"

    @property
    def title(self) -> "str":
        return "Webflow"

    @property
    def primary_color(self) -> "str":
        return "#146EF5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Webflow</title>
     <path d="m24 4.515-7.658 14.97H9.149l3.205-6.204h-.144C9.566
 16.713 5.621 18.973 0 19.485v-6.118s3.596-.213
 5.71-2.435H0V4.515h6.417v5.278l.144-.001
 2.622-5.277h4.854v5.244h.144l2.72-5.244H24Z" />
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
