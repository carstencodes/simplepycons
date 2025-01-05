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


class AnimalPlanetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "animalplanet"

    @property
    def original_file_name(self) -> "str":
        return "animalplanet.svg"

    @property
    def title(self) -> "str":
        return "Animal Planet"

    @property
    def primary_color(self) -> "str":
        return "#0073FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Animal Planet</title>
     <path d="m18.814 5.94-.494.858c2.605.509 4.118 1.618 4.118 2.917
 0 .865-.649 1.696-1.762 1.696-1.699
 0-2.949-2.673-2.949-2.673-.356-.011-.993-.026-.993-.026s-1.822-2.342-4.595-3.168v3.798c.244.205.559.499.855.863-1.252-.757-2.552-1.317-4.847-1.317-2.496
 0-5.547 1.007-7.242 3.763l.178.322c.773-.873 1.968-1.402
 2.006-1.416C1.424 13.012.469 15.427 0 16.998l1.456 1.457a10.687
 10.687 0 0 1 8.055-3.588c2.77 0 5.582 1.157 7.534
 3.157l1.577-1.579c-1.324-2.263-2.924-3.861-2.972-3.909.068.031
 1.487.85 3.975.85 2.312 0 4.375-1.285 4.375-3.203
 0-2.292-1.965-3.745-5.186-4.243" />
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
