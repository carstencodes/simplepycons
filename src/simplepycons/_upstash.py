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


class UpstashIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "upstash"

    @property
    def original_file_name(self) -> "str":
        return "upstash.svg"

    @property
    def title(self) -> "str":
        return "Upstash"

    @property
    def primary_color(self) -> "str":
        return "#00E9A3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Upstash</title>
     <path d="M13.8027 0C11.193 0 8.583.9952 6.5918 2.9863c-3.9823
 3.9823-3.9823 10.4396 0 14.4219 1.9911 1.9911 5.2198 1.9911 7.211 0
 1.991-1.9911 1.991-5.2198 0-7.211L12 12c.9956.9956.9956 2.6098 0
 3.6055-.9956.9955-2.6099.9955-3.6055 0-2.9866-2.9868-2.9866-7.8297
 0-10.8164 2.9868-2.9868 7.8297-2.9868 10.8164
 0l1.8028-1.8028C19.0225.9952 16.4125 0 13.8027 0zM12
 12c-.9956-.9956-.9956-2.6098 0-3.6055.9956-.9955 2.6098-.9955 3.6055
 0 2.9867 2.9868 2.9867 7.8297 0 10.8164-2.9867 2.9868-7.8297
 2.9868-10.8164 0l-1.8028 1.8028c3.9823 3.9822 10.4396 3.9822 14.4219
 0 3.9823-3.9824 3.9823-10.4396
 0-14.4219-.9956-.9956-2.3006-1.4922-3.6055-1.4922-1.3048
 0-2.6099.4966-3.6054 1.4922-1.9912 1.9912-1.9912 5.2198 0 7.211z" />
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
