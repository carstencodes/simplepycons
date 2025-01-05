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


class SpinnakerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spinnaker"

    @property
    def original_file_name(self) -> "str":
        return "spinnaker.svg"

    @property
    def title(self) -> "str":
        return "Spinnaker"

    @property
    def primary_color(self) -> "str":
        return "#139BB4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spinnaker</title>
     <path d="M21.343 0C17.785 8.741 11.317 21.987.815 23.882c10.806
 1.064 19.481-5.327 21.646-8.066C24.627 13.076 21.343 0 21.343 0zM.815
 23.882L.8 23.88v.004l.015-.003zM17.182 5.8C15.409 10.988 10.477
 18.547 5.4 20.39c.885.033 1.74-.019 2.561-.132 3.989-3.221 7.14-8.037
 9.577-12.771-.193-.981-.356-1.687-.356-1.687z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/spinnaker/spinnaker.github'''

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
