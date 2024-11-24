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


class ApacheLuceneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "apachelucene"

    @property
    def original_file_name(self) -> "str":
        return "apachelucene.svg"

    @property
    def title(self) -> "str":
        return "Apache Lucene"

    @property
    def primary_color(self) -> "str":
        return "#019B8F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Apache Lucene</title>
     <path d="M11.476 9.415a.747.747 0 0
 0-.753.577q-.07.264.051.421.123.155.401.155a.8.8 0 0 0
 .366-.083l.058-.23a1 1 0 0 1-.178.08.6.6 0 0 1-.17.025q-.152
 0-.215-.097-.062-.1-.017-.272a.5.5 0 0 1 .158-.27.4.4 0 0 1
 .268-.097q.085-.001.156.023a.5.5 0 0 1 .137.08l.059-.228a.6.6 0 0
 0-.149-.063.7.7 0 0 0-.172-.021m-4.468.021-.702
 1.11h.29l.122-.201h.448l.018.201h.287l-.121-1.11Zm1.19 0-.291
 1.11h.287l.1-.385h.19a.6.6 0 0 0 .35-.094.45.45 0 0 0
 .183-.27q.046-.174-.043-.267-.09-.094-.3-.094zm1.544 0-.701
 1.11h.289l.123-.201h.448l.017.201h.288l-.122-1.11zm2.598 0-.29
 1.11h.286l.123-.471h.423l-.122.471h.286l.291-1.11h-.287l-.112.422h-.422l.111-.422zm1.564
 0-.29
 1.11h.79l.057-.217h-.502l.066-.254h.457l.057-.217h-.46l.056-.207h.486l.057-.215Zm-5.473.207h.158q.083-.001.117.04.036.04.016.115a.2.2
 0 0 1-.076.115.23.23 0 0
 1-.14.04H8.35zm-1.32.053.037.442h-.305Zm2.735 0 .037.442h-.305Zm1.751
 1.352c-.964 0-1.91.782-2.11 1.745-.202.964.415 1.746 1.38 1.746.828 0
 1.643-.58 1.983-1.355h-.852c-.216.32-.585.544-.962.544-.516
 0-.847-.418-.739-.935.108-.516.614-.936 1.13-.936.4 0
 .69.252.749.606h.839c.014-.806-.566-1.415-1.418-1.415m2.219.053-.708
 3.385h2.614l.146-.704H14.08l.125-.596h1.761l.149-.71h-1.762l.141-.673h1.789l.146-.702zm3.35
 0-.71 3.385h.804l.48-2.285.87 2.285h1.021l.708-3.385h-.804l-.469
 2.245-.78-2.245zm3.93 0-.708
 3.385h2.515l.147-.704h-1.689l.123-.596h1.691l.149-.71h-1.691l.14-.673h1.691l.147-.702ZM0
 11.142l.487.723H2.45l.016-.072.135-.65zm3.429 0-.135.65-.143.68-.416
 1.988-.004.026h2.363l.004-.026.137-.65.008-.034H3.704l.551-2.634h-.224Zm2.71
 0-.359 1.726q-.067.323-.066.582h.002l-.004.01q0
 .096.01.184.037.326.199.533a.95.95 0 0 0
 .438.309q.275.1.65.1.372-.001.689-.098.316-.098.565-.305a1.8 1.8 0 0
 0 .426-.528q.177-.32.271-.77l.364-1.743h-.825l-.363
 1.743q-.106.503-.333.747-.224.244-.639.244t-.541-.244q-.127-.243-.022-.747l.366-1.743zm-5.254
 1.42 1.099 1.636.34-1.622.002-.013zm22.362
 1.576v.064h.112v.272h.088v-.272h.111v-.064zm.38
 0v.336h.082v-.246l.076.182h.057l.076-.182v.246H24v-.336h-.11l-.078.18-.076-.18z"
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
