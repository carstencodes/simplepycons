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


class GurobiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gurobi"

    @property
    def original_file_name(self) -> "str":
        return "gurobi.svg"

    @property
    def title(self) -> "str":
        return "Gurobi"

    @property
    def primary_color(self) -> "str":
        return "#EE3524"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gurobi</title>
     <path d="m11.036 0 7.032 1.359L24 18.37 18.37 24 0 17.635 1.805
 5.952 11.036 0Zm12.389 18.239L17.887 2.36l-3.557 7.83 3.88 13.264
 5.215-5.214Zm-5.822-16.46L11.138.528l-8.71 5.617 11.554 3.6
 3.62-7.968Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://cdn.gurobi.com/wp-content/uploads/202'''

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
