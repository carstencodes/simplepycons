#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class MakerbotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "makerbot"

    @property
    def original_file_name(self) -> "str":
        return "makerbot.svg"

    @property
    def title(self) -> "str":
        return "MakerBot"

    @property
    def primary_color(self) -> "str":
        return "#FF1E0D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MakerBot</title>
     <path d="M23.055 7.328c-.604-1.428-1.47-2.714-2.569-3.813C19.382
 2.414 18.1 1.551 16.672.944 15.189.315 13.619 0 12 0c-1.62
 0-3.19.318-4.672.945-1.428.604-2.711 1.47-3.813 2.57C2.414 4.615
 1.551 5.9.943 7.328.315 8.81 0 10.38 0 12c0 1.619.318 3.189.945
 4.671.604 1.429 1.47 2.714 2.569 3.814 1.103 1.1 2.386 1.964 3.813
 2.57C8.81 23.686 10.38 24 12 24c1.619 0 3.189-.314 4.671-.944
 1.429-.601 2.711-1.471 3.814-2.564 1.1-1.095 1.964-2.386
 2.57-3.811.63-1.47.944-3.045.944-4.665
 0-1.619-.314-3.18-.944-4.664v-.024zM12 22.335C6.293 22.335 1.665
 17.707 1.665 12S6.293 1.665 12 1.665 22.335 6.293 22.335 12 17.707
 22.335 12 22.335zm3.242-18.214H8.757c-.922
 0-1.7.324-2.333.975-.635.644-.953 1.425-.953 2.334v10.182c0
 .449.135.81.4 1.095.267.269.615.42 1.051.42.445 0 .805-.135
 1.079-.405.272-.271.409-.63.409-1.08V7.08h2.141v10.529c0
 .445.131.806.391 1.08.259.273.611.411 1.059.411.446 0 .799-.138
 1.059-.411.26-.274.39-.635.39-1.08V7.08h2.142v10.529c0
 .445.135.806.408 1.08.275.273.635.411 1.08.411.435 0 .783-.141
 1.05-.423.268-.28.401-.638.401-1.069V7.426c0-.91-.318-1.688-.953-2.336-.633-.648-1.41-.975-2.334-.975v.006z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.makerbot.com/makerbot-press-asset'''

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