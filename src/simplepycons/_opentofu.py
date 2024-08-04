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


class OpentofuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opentofu"

    @property
    def original_file_name(self) -> "str":
        return "opentofu.svg"

    @property
    def title(self) -> "str":
        return "OpenTofu"

    @property
    def primary_color(self) -> "str":
        return "#FFDA18"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenTofu</title>
     <path d="m10.184 23.25.002-.01-.033-.017-8.388-4.611a1.6841
 1.6841 0 0
 1-.873-1.475V6.864c0-.614.335-1.18.873-1.476l9.424-5.18a1.6868 1.6868
 0 0 1 1.622 0l8.31 4.568.022.012.006.002-.004-.001
 1.09.599c.538.296.873.862.873 1.476v10.273c0 .614-.335 1.179-.873
 1.475l-8.388 4.611-.03.016-1.006.553c-.505.277-1.117.277-1.622
 0l-1.003-.552-.002.01Zm.603-1.158-.005-.001.012.006c.252.123.55-.055.558-.338l.001-9.147c0-.141-.078-.272-.202-.34L2.763
 7.661c-.259-.142-.576.045-.576.341v9.135c0 .141.077.272.201.34l8.394
 4.613.005.002Zm.556-.327Zm0
 0Zm-2.539-4.802-.005.003-1.959-1.031-.003-.004c.001-.003.001-.007.001-.01.023-.305.153-.525.346-.632.194-.107.45-.101.72.041.272.143.508.397.671.691.163.293.252.628.229.935v.007ZM5.71
 15.177l-.005.002-1.96-1.031-.002-.004.001-.01c.022-.304.152-.524.346-.632.194-.107.449-.101.72.042.271.143.508.396.671.69.162.294.252.628.229.935v.008Zm14.981-8.999-.003-.018a.382.382
 0 0 0-.191-.25l-8.31-4.567a.3883.3883 0 0 0-.374 0L3.503
 5.91c-.162.089-.226.265-.193.423l.009.007-.009-.007c.022.1.083.194.183.253l8.32
 4.572c.116.064.258.064.374
 0l8.321-4.573c.151-.089.212-.256.183-.407Zm-17.37.16Zm-.002.002c0-.001-.003-.003-.005-.006-.002-.002-.004-.004-.004-.003l.009.009Zm-.467-1.56-.003.002c.002.004.005.006.005.006l-.002-.008Zm.007.007c-.001.001-.002.001-.003.001h-.002l.005-.001Z"
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
        return '''https://github.com/opentofu/brand-artifacts/b
lob/0d4d0d6050ca0ff06471400bc3249a64c145f659/symbol-only/transparent/S'''

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
        yield from [
            "OpenTF",
            "Terraform",
        ]