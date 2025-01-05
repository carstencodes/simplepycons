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


class MdbookIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mdbook"

    @property
    def original_file_name(self) -> "str":
        return "mdbook.svg"

    @property
    def title(self) -> "str":
        return "mdBook"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>mdBook</title>
     <path d="M22.77 5.343c.023.337 0 .613-.073.817l-4.314
 14.227c-.072.252-.24.445-.504.6a1.67 1.67 0 0 1-.805.23H3.772c-1.154
 0-1.839-.337-2.079-1.01-.096-.264-.096-.469.012-.625.108-.144.288-.216.553-.216h12.52c.89
 0 1.514-.168 1.85-.493.337-.324.686-1.07
 1.034-2.21l3.954-13.05c.216-.71.12-1.334-.265-1.875-.384-.54-.937-.817-1.646-.817H8.735c-.12
 0-.373.048-.734.132l.012-.048A2.458 2.458 0 0 0 7.33.933a.979.979 0 0
 0-.517.168 1.794 1.794 0 0 0-.385.337c-.096.12-.18.264-.276.456a5.76
 5.76 0 0 0-.228.517 7.95 7.95 0 0
 1-.217.505c-.084.18-.156.324-.24.444-.06.073-.144.18-.24.3-.096.121-.193.241-.265.337a.776.776
 0 0
 0-.132.265c-.024.084-.012.216.024.384.036.168.048.289.048.373-.036.36-.168.829-.396
 1.394-.229.564-.433.973-.613 1.213a5.201 5.201 0 0
 1-.312.325c-.169.168-.277.312-.313.444-.036.048-.036.18-.012.409.036.216.048.372.036.456-.036.325-.156.757-.36
 1.298a9.47 9.47 0 0 1-.601
 1.322c-.024.06-.108.168-.24.336-.133.168-.217.3-.24.409-.025.072-.013.216.011.408.024.193.024.337-.012.433-.072.36-.216.805-.432
 1.322-.217.516-.433.949-.65
 1.321-.06.097-.131.205-.24.337-.096.132-.18.24-.24.336a.927.927 0 0
 0-.12.3.53.53 0 0 0
 .048.277c.036.132.048.228.048.313-.012.132-.024.312-.06.528-.024.216-.048.349-.048.385-.216.576-.204
 1.19.024 1.826.264.745.745 1.382 1.43 1.899.685.516 1.406.769
 2.139.769H17.05c.625 0 1.214-.205 1.767-.625.553-.42.925-.937
 1.105-1.55l3.966-13.05c.216-.696.12-1.31-.265-1.862-.204-.3-.48-.505-.853-.649ZM7.16
 15.677l1.707-5.143h1.297c.457 0 3.46-.204 3.052 2.103-.408
 2.307-2.259 3.028-4.422
 3.052-2.162.024-1.634-.012-1.634-.012zm2.283-.721c.565-.012
 2.271-.349 2.656-2.055.384-1.706-1.382-1.61-1.382-1.61h-1.07l-1.225
 3.665c.012.012.469.012 1.021 0zm-.396-5.78 1.646-5.107h1.178l.096
 4.086 2.835-4.086h1.19l-1.634 5.107h-.853l1.502-4.253-2.944
 4.253h-.817l-.096-4.205-1.298 4.205z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/rust-lang/mdBook/blob/cdfa'''

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
