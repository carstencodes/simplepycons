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


class SagemathIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sagemath"

    @property
    def original_file_name(self) -> "str":
        return "sagemath.svg"

    @property
    def title(self) -> "str":
        return "SageMath"

    @property
    def primary_color(self) -> "str":
        return "#3333FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SageMath</title>
     <path d="M8.122 0a.9.9 0 0 0-.9.9.9.9 0 0 0 .165.514l-2.21
 2.563a1.094 1.094 0 0 0-.307-.044 1.094 1.094 0 0 0-1.093 1.094 1.094
 1.094 0 0 0 .006.091l-1.95 1.284a.9.9 0 0 0-.516-.165.9.9 0 0
 0-.9.9.9.9 0 0 0 .4.746L.46 14.586a.705.705 0 0 0-.375.62.705.705 0 0
 0 .706.706.705.705 0 0 0 .095-.007l4.889 5.016a.705.705 0 0
 0-.004.051.705.705 0 0 0 .705.705.705.705 0 0 0 .386-.115l2.651
 1.426a.9.9 0 0 0-.008.113.9.9 0 0 0 .9.899.9.9 0 0 0
 .895-.819l7.183-2.097a.9.9 0 0 0 .718.361.9.9 0 0 0 .9-.9.9.9 0 0
 0-.197-.556l3.11-6.845a.9.9 0 0 0 .899-.9.9.9 0 0
 0-.723-.879l-.975-3.259a.705.705 0 0 0 .256-.543.705.705 0 0
 0-.705-.705.705.705 0 0 0-.137.015L17.163 1.4a.705.705 0 0 0
 .011-.12.705.705 0 0 0-.705-.706.705.705 0 0 0-.549.266L8.968.6a.9.9
 0 0 0-.846-.6zm.84 1.218 6.825.235a.705.705 0 0 0
 .276.4l-.161.768a1.094 1.094 0 0 0-.75.605l-7.64.89.512-2.324a.9.9 0
 0 0 .098.007.9.9 0 0 0 .84-.58zm7.82.692 4.356 5.337a.705.705 0 0
 0-.076.316.705.705 0 0 0 .225.515L20.93 9.08l-3.82-4.886a1.094 1.094
 0 0 0 .127-.51 1.094 1.094 0 0 0-.713-1.022l.149-.709a.705.705 0 0 0
 .11-.044zm-9.132.145-.462 2.099-1.48.172a1.094 1.094 0 0
 0-.008-.01zm7.554 2.408-2.215 8.64a1.363 1.363 0 0 0-.178.054L7.097
 6.692l2.663-.297a.705.705 0 0 0 .618.371.705.705 0 0 0
 .705-.704.705.705 0 0
 0-.02-.16l3.747-1.393zm-1.685.196-2.59.964a.705.705 0 0
 0-.55-.266.705.705 0 0 0-.705.705.705.705 0 0 0
 .002.031l-2.664.298.22-.999zm2.877.125 4.166 5.33-.86 2.417-5.233
 1.218a1.363 1.363 0 0
 0-.282-.347zm-9.489.646-.184.84-.655-.742zm-2.892.275a1.094 1.094 0 0
 0 .209.2l-.156.816-1.878.21a.9.9 0 0 0-.005-.022zm.797.41a1.094 1.094
 0 0 0 .058.005 1.094 1.094 0 0 0
 .071-.002l.407.46-.639.071zm.786.745.797.902-.343 1.56a.705.705 0 0
 0-.679.703.705.705 0 0 0 .25.538l-2.355 3.614
 1.38-7.21zm-1.59.178-1.496 7.808a.9.9 0 0
 0-.59.423l-.427-.08a.705.705 0 0 0-.415-.625l.347-6.535a.9.9 0 0 0
 .782-.79zm2.64 1.01 5.328 6.029a1.363 1.363 0 0
 0-.02.095l-8.62.925a.9.9 0 0 0-.2-.153L5.9 10.705a.705.705 0 0 0
 .18.024.705.705 0 0 0 .704-.704.705.705 0 0
 0-.428-.647zm14.91.188a.705.705 0 0 0 .057.013l.827
 2.766-1.287-1.646zm-.77 2.166 1.24 1.588-1.969.458zm1.31 2.522-2.828
 6.224.057-3.885a.66.66 0 0 0 .546-.65.66.66 0 0
 0-.374-.593l.19-.535zm-2.766.644-.138.388a.66.66 0 0 0-.64.658.66.66
 0 0 0 .464.63l-.065 4.438a.9.9 0 0 0-.525.41l-3.924-.847a.705.705 0 0
 0-.705-.699.705.705 0 0 0-.702.67l-.961.235 1.183-3.66a1.363 1.363 0
 0 0 1.314-1.13zm-7.23 1.52a1.363 1.363 0 0 0 .34.402l-1.363
 4.22-2.927.717-4.629-4.353a.9.9 0 0 0
 .026-.068zm-10.4.768.109.02a.9.9 0 0 0 .029.121zm.697.715a.9.9 0 0 0
 .296.053.9.9 0 0 0 .06-.002l3.902 3.67a.705.705 0 0
 0-.18-.025.705.705 0 0 0-.372.107zm10.75 2.95a.705.705 0 0 0
 .65.435.705.705 0 0 0 .64-.41l3.453.746-6.655
 1.943.787-2.439zm-2.181.534-.697 2.157a.9.9 0 0 0-.173.046L8.42
 20.679zm-3.62.887.446.42-.615-.331a.705.705 0 0 0 .002-.049z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/sagemath/artwork/blob/dc51'''

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
