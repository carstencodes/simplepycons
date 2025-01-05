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


class OppoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "oppo"

    @property
    def original_file_name(self) -> "str":
        return "oppo.svg"

    @property
    def title(self) -> "str":
        return "OPPO"

    @property
    def primary_color(self) -> "str":
        return "#2D683D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OPPO</title>
     <path d="M2.85 12.786h-.001C1.639 12.774.858 12.2.858
 11.321s.781-1.452 1.99-1.465c1.21.013 1.992.588 1.992 1.465s-.782
 1.453-1.99 1.465zm.034-3.638h-.073C1.156 9.175 0 10.068 0 11.32s1.156
 2.147 2.811 2.174h.073c1.655-.027 2.811-.921 2.811-2.174S4.54 9.175
 2.885 9.148zm18.27 3.638c-1.21-.012-1.992-.587-1.992-1.465s.782-1.452
 1.991-1.465c1.21.013 1.991.588 1.991 1.465s-.781 1.453-1.99
 1.465zm.035-3.638h-.073c-1.655.027-2.811.92-2.811 2.173s1.156 2.147
 2.81 2.174h.074C22.844 13.468 24 12.574 24
 11.32s-1.156-2.146-2.811-2.173zm-6.126
 3.638c-1.21-.012-1.99-.587-1.99-1.465s.78-1.452 1.99-1.465c1.21.013
 1.991.588 1.991 1.465s-.781 1.453-1.99
 1.465zm.036-3.638h-.073c-.789.013-1.464.222-1.955.574v-.37h-.857v5.5h.857v-1.931c.49.351
 1.166.56 1.954.574h.074c1.655-.027 2.81-.921
 2.81-2.174s-1.155-2.146-2.81-2.173zm-6.144
 3.638c-1.21-.012-1.99-.587-1.99-1.465s.78-1.452 1.99-1.465c1.21.013
 1.991.588 1.991 1.465s-.781 1.453-1.99
 1.465zm.037-3.638H8.92c-.789.013-1.464.222-1.955.574v-.37h-.856v5.5h.856v-1.931c.491.351
 1.166.56 1.955.574a3.728 3.728 0 0 0 .073 0c1.655-.027 2.811-.921
 2.811-2.174s-1.156-2.146-2.81-2.173z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.figma.com/community/file/83281597'''

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
