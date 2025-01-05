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


class BoeingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "boeing"

    @property
    def original_file_name(self) -> "str":
        return "boeing.svg"

    @property
    def title(self) -> "str":
        return "Boeing"

    @property
    def primary_color(self) -> "str":
        return "#1D439C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Boeing</title>
     <path d="M6.9044 17.2866a6.0512 6.0512 0
 01-3.7595-1.3008c1.2048-2.7146 3.6545-6.3581 6.998-9.9166a6.0702
 6.0702 0 012.2617 7.729c-1.0599-.49-2.0497-1.106-2.8876-1.8798l1.8307
 3.4375a6.0582 6.0582 0 01-4.4433 1.9307M.8292 11.2115a6.0752 6.0752 0
 016.0762-6.0772c.8998 0 1.7527.196 2.5226.546-3.2935 2.9095-5.8432
 6.293-7.353 9.2177a6.0512 6.0512 0 01-1.2458-3.6875m12.3403
 2.9126a6.862 6.862 0
 00.6419-2.9126c0-2.3997-1.2248-4.5144-3.0846-5.7532a49.6072 49.6072 0
 013.5825-3.3416A31.1727 31.1727 0 0010.11 5.0903a6.907 6.907 0
 00-8.4368 10.6265C.3493 18.5795.1193 20.8781 1.285 21.654c1.2489.832
 3.9625-.6769 5.5903-3.1345 0 0-2.5177 2.2736-3.9015
 1.7517-.8519-.322-.8549-1.6248-.152-3.4925a6.871 6.871 0 004.0835
 1.3378c1.8937 0 3.6065-.7599 4.8533-1.9917l.245.462c3.0095-.245
 11.9963-.483 11.9963-.483 0-.431-5.9502-.04-10.8325-1.9797" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Boein'''

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
