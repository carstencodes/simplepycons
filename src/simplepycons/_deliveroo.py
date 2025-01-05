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


class DeliverooIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deliveroo"

    @property
    def original_file_name(self) -> "str":
        return "deliveroo.svg"

    @property
    def title(self) -> "str":
        return "Deliveroo"

    @property
    def primary_color(self) -> "str":
        return "#00CCBC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Deliveroo</title>
     <path d="M16.861 0l-1.127 10.584L13.81 1.66 7.777 2.926l1.924
 8.922-8.695 1.822 1.535 7.127L17.832 24l3.498-7.744L22.994.636 16.861
 0zM11.39 13.61a.755.755 0
 01.322.066c.208.093.56.29.63.592.103.434.004.799-.312
 1.084v.002c-.315.284-.732.258-1.174.113-.441-.145-.637-.672-.47-1.309.124-.473.71-.544
 1.004-.549zm4.142.548c.447-.012.832.186 1.05.543.217.357.107.75-.122
 1.143h-.002c-.229.392-.83.445-1.422.16-.399-.193-.397-.684-.353-.983a.922.922
 0 01.193-.447c.142-.177.381-.408.656-.416Z" />
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
