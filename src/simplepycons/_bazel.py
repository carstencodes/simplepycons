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


class BazelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bazel"

    @property
    def original_file_name(self) -> "str":
        return "bazel.svg"

    @property
    def title(self) -> "str":
        return "Bazel"

    @property
    def primary_color(self) -> "str":
        return "#43A047"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bazel</title>
     <path d="m11.7473 23.8198-5.4987-5.4987v-5.5349l5.4987
 5.4986v5.535zm-.1036-17.6412-.0001-.0001.1768-.1768L5.9986.1799.1768
 6.0018l.0001.0001 5.8217 5.8271 5.6451-5.6504zM0 6.5323v5.5347l5.7486
 5.7539v-5.5347l-.1035-.1035.0001-.0001L0 6.5323zm17.6478
 5.6504-5.6505-5.6505-5.6452 5.6504 5.6452 5.6453 5.6505-5.6452zm.1036
 5.8885v-5.2853l-5.5042 5.4991v5.5351l5.5042-5.4991v-.2498zM24
 6.5323l-5.6451 5.6503.0001.0001-.1036.1035v5.5346L24
 12.067V6.5323zm-.1769-.5304.0001-.0001L18.0014.18l-5.8273 5.822
 5.8273 5.8272 5.8217-5.8273z" />
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
