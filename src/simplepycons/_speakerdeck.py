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


class SpeakerDeckIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "speakerdeck"

    @property
    def original_file_name(self) -> "str":
        return "speakerdeck.svg"

    @property
    def title(self) -> "str":
        return "Speaker Deck"

    @property
    def primary_color(self) -> "str":
        return "#009287"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Speaker Deck</title>
     <path d="M10.025 13.875H4.687a4.688 4.688 0 0 1
 0-9.375h6.227a1.875 1.875 0 0 1 0 3.75H4.592a.937.937 0 1 0 0
 1.875h5.337a4.687 4.687 0 1 1 0 9.375H1.875a1.875 1.875 0 0 1
 0-3.75h8.15a.938.938 0 0 0 0-1.875zM13.97 19.5a5.635 5.635 0 0 0
 2.396-3.75h3.026a.93.93 0 0 0 .921-.938V9.189a.93.93 0 0
 0-.921-.938h-5.497c.438-.498.704-1.155.704-1.875s-.266-1.377-.704-1.875h6.418C22.35
 4.5 24 6.179 24 8.25v7.5c0 2.071-1.65 3.75-3.687 3.75H13.97z" />
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
