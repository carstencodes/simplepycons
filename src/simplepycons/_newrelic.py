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


class NewRelicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "newrelic"

    @property
    def original_file_name(self) -> "str":
        return "newrelic.svg"

    @property
    def title(self) -> "str":
        return "New Relic"

    @property
    def primary_color(self) -> "str":
        return "#1CE783"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>New Relic</title>
     <path d="M8.0015 14.3091v7.384L12.0008 24V12.0008L1.6078
 5.9996v4.6167ZM12.0008 0 2.8232 5.2976 6.8209 7.606l5.1799-2.9893
 6.3936 3.6913v7.384l-5.1783 2.9908v4.6167l9.176-5.2991V5.9996Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://newrelic.com/about/media-assets#guide'''
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
