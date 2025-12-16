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


class SlackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "slack"

    @property
    def original_file_name(self) -> "str":
        return "slack.svg"

    @property
    def title(self) -> "str":
        return "Slack"

    @property
    def primary_color(self) -> "str":
        return "#4A154B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Slack</title>
     <path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0
 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313
 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521
 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0
 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528
 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834
 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521
 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1
 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528
 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522
 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527
 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0
 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523
 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0
 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523
 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528
 2.528 0 0 1-2.522 2.523h-6.313z" />
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
