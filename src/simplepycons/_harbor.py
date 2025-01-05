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


class HarborIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "harbor"

    @property
    def original_file_name(self) -> "str":
        return "harbor.svg"

    @property
    def title(self) -> "str":
        return "Harbor"

    @property
    def primary_color(self) -> "str":
        return "#60B932"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Harbor</title>
     <path d="m7.006 15.751 4.256
 1.876.066.805-4.388-1.934.066-.747zm.304-3.435h-.605V11.21h.381V8.95h-.381v-.649l2.118-2.073v-.146c0-.11.09-.2.2-.2.11
 0 .2.09.2.2v.146l2.12 2.073v.65h-.382v2.259h.381v1.106h-.514l.27
 3.313L7.17
 13.9l.14-1.583zm.39-1.106h.628v-.965c0-.383.313-.696.695-.696s.696.313.696.696v.965h.628V8.95H7.7v2.26zM6.89
 17.05l-.066.747 4.618 2.035-.066-.805-4.486-1.977zm.23-2.6-.066.747
 4.158 1.832-.065-.805-4.026-1.774zM24 12c0 6.617-5.383 12-12 12S0
 18.617 0 12 5.383 0 12 0s12 5.383 12 12zm-2.43-.715a9.682 9.682 0 0
 0-.223-1.523l-9.751.332 8.801-2.828-.019-.037A9.802 9.802 0 0 0 19.23
 5.59l-7.786 4.03 5.712-5.941a9.675 9.675 0 0 0-5.14-1.474c-5.371
 0-9.74 4.369-9.74 9.74 0 3.38 1.73 6.362 4.35 8.11l.151-1.704 4.715
 2.078.102 1.246c.14.006.28.01.422.01 4.646 0 8.54-3.27
 9.507-7.63l-10.08-3.497 10.128.727" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://github.com/cncf/artwork/blob/ff2b2b52'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/cncf/artwork/blob/ff2b2b52
16e22f001ddd444ca580c484dd10302e/projects/harbor/icon/black/harbor-ico'''

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
